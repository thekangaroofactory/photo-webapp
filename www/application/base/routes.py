from flask import Blueprint
from flask import render_template

# Blueprint Configuration
base_bp = Blueprint('base_bp', __name__, template_folder='templates')


@base_bp.route("/")
def index():
    # return "Index page from Base module"
    return render_template('home.html', param="Ceci est un paragraphe dynamique retourné par Python.")
