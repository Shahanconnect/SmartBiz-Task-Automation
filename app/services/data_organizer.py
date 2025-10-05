from flask import Blueprint, render_template, session, redirect, url_for, request

data_organizer_bp = Blueprint("data_organizer", __name__)

@data_organizer_bp.route("/data-organizer")
def data_organizer():
    scraped_products = session.get("scraped_products", [])
    return render_template("data_organizer.html", scraped_products=scraped_products)


@data_organizer_bp.route("/delete-product/<int:index>", methods=["POST"])
def delete_product(index):
    scraped_products = session.get("scraped_products", [])
    if 0 <= index < len(scraped_products):
        del scraped_products[index]
        session["scraped_products"] = scraped_products
    return redirect(url_for("data_organizer.data_organizer"))


@data_organizer_bp.route("/clear-all-products", methods=["POST"])
def clear_all_products():
    session["scraped_products"] = []
    return redirect(url_for("data_organizer.data_organizer"))
