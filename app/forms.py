from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, TextAreaField,
    FloatField, DecimalField, SelectField, IntegerField,
    FieldList, FormField
)
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo, Regexp, URL, Optional
)

# ------------------- Signup Form ------------------- #
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=25, message="Username must be between 3 and 25 characters.")
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Invalid email address.")
    ])
    phone = StringField('Phone Number', validators=[
        DataRequired(),
        Regexp(r'^[0-9]{10}$', message="Phone number must be 10 digits.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, message="Password must be at least 6 characters long.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match.")
    ])
    submit = SubmitField('Sign Up')


# ------------------- Login Form ------------------- #
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Invalid email address.")
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# ------------------- Forgot Password Form ------------------- #
class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Invalid email address.")
    ])
    submit = SubmitField('Reset Password')


# ------------------- Reset Password Form ------------------- #
class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(),
        Length(min=6, message='Password must be at least 6 characters long.')
    ])
    confirm_password = PasswordField('Confirm New Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Reset Password')


# ------------------- Product Description Generator ------------------- #
class ProductDescriptionForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_category = StringField('Product Category', validators=[DataRequired()])
    product_features = TextAreaField('Product Features (comma-separated)', validators=[DataRequired()])
    submit = SubmitField('Generate Description')


# ------------------- Price Alert Form ------------------- #
class PriceAlertForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_url = StringField('Product URL', validators=[DataRequired(), URL()])
    target_price = DecimalField('Target Price', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Set Alert')


# ------------------- Scraper Form ------------------- #
class ScraperForm(FlaskForm):
    url = StringField("Enter Product Page URL", validators=[DataRequired(), URL()])
    submit = SubmitField("Scrape")


# ------------------- Task Automator Form ------------------- #
class TaskForm(FlaskForm):
    task = SelectField('Task', choices=[
        ('', '-- Choose an action --'),
        ('notepad', 'Open Notepad'),
        ('calculator', 'Open Calculator'),
        ('webpage', 'Open Webpage'),
        ('explorer', 'Open File Explorer'),
        ('cmd', 'Open Command Prompt'),
        ('system_info', 'Open System Information'),
        ('restart', 'Restart Computer'),
        ('shutdown', 'Shutdown Computer'),
        ('email', 'Send Email')
    ])
    url = StringField('Web URL', validators=[Optional()])
    recipient = StringField('Recipient Email', validators=[Optional()])
    subject = StringField('Subject', validators=[Optional()])
    message = TextAreaField('Message', validators=[Optional()])
    submit = SubmitField('Execute Task')


# ------------------- Invoice Generator Form ------------------- #
class InvoiceForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    company_email = StringField('Company Email', validators=[DataRequired(), Email()])
    client_name = StringField('Client Name', validators=[DataRequired()])
    client_email = StringField('Client Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Generate Invoice')


# ------------------- Item Entry Form (For Invoice) ------------------- #
class ItemForm(FlaskForm):
    description = StringField('Item Description', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = DecimalField('Unit Price', validators=[DataRequired()])
