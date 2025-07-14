from flask import (
    Flask, render_template, redirect, url_for, flash,
    request, Blueprint, current_app, jsonify, session,
    send_file, abort, make_response
)
from flask_login import (
    login_user, login_required, logout_user, current_user
)
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature

from datetime import datetime
from io import BytesIO
import json
from decimal import Decimal
import os

# Project modules
from app import db
from app.forms import (
    SignupForm, LoginForm, ProductDescriptionForm, ForgotPasswordForm,
    ResetPasswordForm, PriceAlertForm, ScraperForm, InvoiceForm, TaskForm
)
from app.models import User, PriceAlert, ProductDescription
from app.services.scraper import scrape_product_details
from app.services.price_alert import check_price_alerts
from app.services.description_service import generate_product_description

from app.services.task_automator import (
    run_notepad_task,
    open_calculator,
    open_webpage,
    open_file_explorer,
    open_command_prompt,
    open_system_information,
    restart_computer,
    shutdown_computer,
    
)

from dotenv import load_dotenv
load_dotenv()

# Mail & Token setup
mail = Mail()
s = URLSafeTimedSerializer(os.getenv('FLASK_SECRET_KEY'))  
task_automator_bp = Blueprint('task_automator', __name__)



def register_routes(app):
    app.register_blueprint(task_automator_bp, url_prefix='/task-automator')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        form = SignupForm()
        if form.validate_on_submit():
            existing_user = User.query.filter(
                (User.username == form.username.data) | (User.email == form.email.data)
            ).first()
            if existing_user:
                flash("Username or email already exists.", "danger")
                return render_template('signup.html', form=form)

            user = User(
                username=form.username.data,
                email=form.email.data,
                phone=form.phone.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            flash("Account created successfully!", "success")
            return redirect(url_for('login'))

        return render_template('signup.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                if not user.is_active:
                    flash("Account is deactivated. Contact support.", "warning")
                    return redirect(url_for('login'))

                login_user(user)
                flash("Login successful!", "success")

            # Redirect based on admin flag (fallback to email if needed)
                if user.is_admin :
                    return redirect(url_for('admin_dashboard'))
                else:
                    return redirect(url_for('user_dashboard'))
            else:
                flash("Invalid email or password", "danger")
        return render_template('login.html', form=form)



    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash("Logged out successfully.", "info")
        return redirect(url_for('login'))

    @app.route('/forgot_password', methods=['GET', 'POST'])
    def forgot_password():
        form = ForgotPasswordForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                token = s.dumps(user.email, salt='password-reset-salt')
                link = url_for('reset_password', token=token, _external=True)

                msg = Message(
                    'Password Reset Request',
                    recipients=[user.email],
                    sender='noreply@smartbiz.com'
                )
                msg.body = f"Click the link to reset your password: {link}"
                mail.send(msg)

                flash("Reset link sent to your email.", "success")
                return redirect(url_for('login'))
            else:
                flash("Email not found.", "danger")

        return render_template('forgot_password.html', form=form)

    @app.route('/reset_password/<token>', methods=['GET', 'POST'])
    def reset_password(token):
        try:
            email = s.loads(token, salt='password-reset-salt', max_age=3600)
        except SignatureExpired:
            flash("Reset link expired.", "danger")
            return redirect(url_for('forgot_password'))
        except BadSignature:
            flash("Invalid reset link.", "danger")
            return redirect(url_for('forgot_password'))

        form = ResetPasswordForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=email).first()
            if user:
                user.set_password(form.password.data)
                db.session.commit()
                flash("Password updated successfully!", "success")
                return redirect(url_for('login'))

        return render_template('reset_password.html', form=form)

    @app.route('/user-dashboard')
    @login_required
    def user_dashboard():
        return render_template('user_dashboard.html')

    @app.route('/user-dashboard/profile', methods=['GET', 'POST'])
    @login_required
    def user_profile():
        return render_template('user_profile.html')

    @app.route('/product-description', methods=['GET', 'POST'])
    @login_required
    def product_description():
        form = ProductDescriptionForm()
        description = None

        if form.validate_on_submit():
            product_name = form.product_name.data
            category = form.product_category.data
            features = form.product_features.data

            description = generate_product_description(product_name, category, features)

            entry = ProductDescription(
                user_id=current_user.id,
                product_name=product_name,
                product_category=category,
                product_features=features,
                description=description,
                created_at=datetime.utcnow()
            )
            db.session.add(entry)
            db.session.commit()

            flash("Description generated and saved!", "success")
            return redirect(url_for('product_description', history_id=entry.id))

        history_id = request.args.get('history_id')
        if history_id and history_id.isdigit():
            entry = ProductDescription.query.filter_by(user_id=current_user.id, id=int(history_id)).first()
            if entry:
                description = entry.description

        history = ProductDescription.query.filter_by(user_id=current_user.id).order_by(
            ProductDescription.created_at.desc()
        ).all()

        return render_template(
            'product_description.html',
            form=form,
            description=description,
            description_history=history,
            selected_history_id=int(history_id) if history_id and history_id.isdigit() else None
        )

    @app.route('/delete-description/<int:description_id>', methods=['POST'])
    @login_required
    def delete_description(description_id):
        desc = ProductDescription.query.get_or_404(description_id)
        if desc.user_id != current_user.id:
            flash("Unauthorized.", "danger")
            return redirect(url_for('product_description'))

        db.session.delete(desc)
        db.session.commit()
        flash("Description deleted.", "success")
        return redirect(url_for('product_description'))

    @app.route('/delete-all-descriptions', methods=['POST'])
    @login_required
    def delete_all_descriptions():
        ProductDescription.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        flash("All descriptions deleted.", "success")
        return redirect(url_for('product_description'))

    @app.route('/price-alert', methods=['GET', 'POST'])
    @login_required
    def price_alert():
        form = PriceAlertForm()
        if form.validate_on_submit():
            alert = PriceAlert(
                user_id=current_user.id,
                product_name=form.product_name.data,
                product_url=form.product_url.data,
                target_price=form.target_price.data,
                email=form.email.data
            )
            db.session.add(alert)
            db.session.commit()

            check_price_alerts(current_app)

            flash("Price alert created and checked!", "success")
            return redirect(url_for('price_alert'))

        alerts = PriceAlert.query.filter_by(user_id=current_user.id).all()
        return render_template('price_alert.html', form=form, alerts=alerts)

    @app.route('/delete-alert/<int:alert_id>', methods=['POST'])
    @login_required
    def delete_alert(alert_id):
        alert = PriceAlert.query.get_or_404(alert_id)
        if alert.user_id != current_user.id:
            flash("Unauthorized action.", "danger")
            return redirect(url_for('price_alert'))

        db.session.delete(alert)
        db.session.commit()
        flash("Alert deleted.", "success")
        return redirect(url_for('price_alert'))

    @app.route('/scrape', methods=['GET', 'POST'])
    @login_required
    def scrape():
        form = ScraperForm()
        data = None
        scrape_history = session.get('scrape_history', [])

        if form.validate_on_submit():
            url = form.url.data
            result = scrape_product_details(url)
            if result['status'] == 'success':
                data = result
                scrape_history.insert(0, result)
                session['scrape_history'] = scrape_history[:10]
            else:
                flash(f"Error: {result['message']}", "danger")

        elif request.args.get('history_index'):
            index = request.args.get('history_index')
            if index.isdigit():
                idx = int(index)
                if 0 <= idx < len(scrape_history):
                    data = scrape_history[idx]

        return render_template('scrape.html', form=form, data=data, scrape_history=scrape_history)

    @app.route('/delete-scrape-entry/<int:index>', methods=['POST'])
    @login_required
    def delete_scrape_entry(index):
        scrape_history = session.get('scrape_history', [])
        if 0 <= index < len(scrape_history):
            del scrape_history[index]
            session['scrape_history'] = scrape_history
            flash("Scrape entry deleted.", "success")
        return redirect(url_for('scrape'))

    @app.route('/delete-scrape-history', methods=['POST'])
    @login_required
    def delete_scrape_history():
        session['scrape_history'] = []
        flash("Scrape history cleared.", "success")
        return redirect(url_for('scrape'))


    @app.route('/delete-all-alerts', methods=['POST'])
    @login_required
    def delete_all_alerts():
        alerts = PriceAlert.query.filter_by(user_id=current_user.id).all()
        for alert in alerts:
            db.session.delete(alert)
        db.session.commit()
        flash("All alerts deleted successfully.", "info")
        return redirect(url_for('price_alert'))









    

    @app.route('/invoice-form', methods=['GET', 'POST'])
    @login_required
    def invoice_form():
        form = InvoiceForm()
        if form.validate_on_submit():
            session['invoice_data'] = {
                'company_name': form.company_name.data,
                'company_email': form.company_email.data,
                'client_name': form.client_name.data,
                'client_email': form.client_email.data,
                'item_description': request.form.getlist('item_description[]'),
                'item_qty': request.form.getlist('item_qty[]'),
                'item_price': request.form.getlist('item_price[]')
            }
            return redirect(url_for('invoice_preview'))
        return render_template('invoice_form.html', form=form)

    @app.route('/invoice-preview', methods=['GET'])
    @login_required
    def invoice_preview():
        data = session.get('invoice_data')
        if not data:
            return redirect(url_for('invoice_form'))

        descriptions = data.get('item_description', [])
        qtys = data.get('item_qty', [])
        prices = data.get('item_price', [])

        items = []
        total = 0
        for desc, qty, price in zip(descriptions, qtys, prices):
            try:
                qty = int(qty)
                price = float(price)
            except ValueError:
                qty = 0
                price = 0.0
            total += qty * price
            items.append({'description': desc, 'qty': qty, 'price': price, 'total': qty * price})

        return render_template('invoice_preview.html',
            company_name=data.get('company_name'),
            company_email=data.get('company_email'),
            client_name=data.get('client_name'),
            client_email=data.get('client_email'),
            invoice_date=datetime.now().strftime('%Y-%m-%d'),
            items=items,
            total_amount=total
        )




    @app.route('/task-automator', methods=['GET', 'POST'])
    @login_required
    def task_automator():
        form = TaskForm()

        if form.validate_on_submit():
            task = request.form.get('task')
            url = request.form.get('url')
            recipient = request.form.get('recipient')
            subject = request.form.get('subject')
            message = request.form.get('message')

            try:
                if task == 'notepad':
                    run_notepad_task()
                elif task == 'calculator':
                    open_calculator()
                elif task == 'webpage' and url:
                    open_webpage(url)
                elif task == 'explorer':
                    open_file_explorer()
                elif task == 'cmd':
                    open_command_prompt()
                elif task == 'system_info':
                    open_system_information()
                elif task == 'restart':
                    restart_computer()
                elif task == 'shutdown':
                    shutdown_computer()

                else:
                    flash('Invalid task or missing input.', 'danger')
                    return redirect(url_for('task_automator'))

                flash('Task executed successfully!', 'success')
            except Exception as e:
                flash(f'Task execution failed: {e}', 'danger')

            return redirect(url_for('task_automator'))

        return render_template('task_automator.html', form=form)
    
    
    
    
    @app.route('/admin')
    @login_required
    def admin_dashboard():
        if not current_user.is_admin:
        
            return redirect(url_for('user_dashboard'))
        return render_template('admin_dashboard.html')



    @app.route('/admin/user-management')
    @login_required
    def user_management():
        if current_user.is_admin:

        
            return redirect(url_for('user_dashboard'))

        search_query = request.args.get('search', '').strip()
        if search_query:
            users = User.query.filter(User.username.ilike(f"%{search_query}%")).all()
        else:
            users = User.query.all()

        return render_template('user_management.html', users=users)



    @app.route('/admin/toggle-admin/<int:user_id>')
    @login_required
    def toggle_admin(user_id):
        if not current_user.is_admin:
            flash("Access denied. Admins only.", "danger")
            return redirect(url_for('user_dashboard'))
        user = User.query.get_or_404(user_id)
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f"Admin status for {user.email} toggled.", "info")
        return redirect(url_for('user_management'))


    @app.route('/admin/toggle-active/<int:user_id>')
    @login_required
    def toggle_active(user_id):
        if not current_user.is_admin:
            flash("Access denied. Admins only.", "danger")
            return redirect(url_for('user_dashboard'))
        user = User.query.get_or_404(user_id)
        user.is_active = not user.is_active
        db.session.commit()
        flash(f"Active status for {user.email} toggled.", "info")
        return redirect(url_for('user_management'))


    @app.route('/admin/delete-user/<int:user_id>')
    @login_required
    def delete_user(user_id):
        if not current_user.is_admin:
            flash("Access denied. Admins only.", "danger")
            return redirect(url_for('user_dashboard'))
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        flash(f"User {user.email} has been deleted.", "danger")
        return redirect(url_for('user_management'))





    @app.route('/admin/services', methods=['GET', 'POST'])
    @login_required
    def service_management():
        if not current_user.is_admin :
            flash("Access denied.", "danger")
            return redirect(url_for('user_dashboard'))

        users = User.query.all()
        return render_template('admin_services.html', users=users)

    @app.route('/admin/toggle_service/<int:user_id>/<string:service_name>', methods=['POST'])
    @login_required
    def toggle_service(user_id, service_name):
        if not current_user.is_admin:
            flash("Access denied.", "danger")
            return redirect(url_for('user_dashboard'))

        user = User.query.get(user_id)
        if not user:
            flash("User not found.", "danger")
            return redirect(url_for('service_management'))


        if hasattr(user, service_name):
            setattr(user, service_name, not getattr(user, service_name))
            db.session.commit()
            flash(f"{service_name.replace('_', ' ').title()} updated for {user.username}.", "success")
        else:
            flash("Invalid service.", "danger")

        return redirect(url_for('service_management'))



    @app.route('/toggle_service_all/<service_name>/<action>', methods=['POST'])
    @login_required
    def toggle_service_all(service_name, action):

        value = True if action == 'activate' else False
        User.query.update({getattr(User, service_name): value})
        db.session.commit()
        flash(f"{service_name.replace('_', ' ').title()} updated for all users!", "info")
        return redirect(url_for('service_management'))
