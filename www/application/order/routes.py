
from flask import Blueprint, current_app
from flask import render_template
from flask_login import login_required

from application.order.orders import get_orders
from application.admin.tools import admin_required

app = current_app

# Blueprint Configuration
order_bp = Blueprint('order_bp', __name__, template_folder='templates')


@order_bp.route('/order', methods=['GET'])
@login_required
@admin_required
def show_orders():
    """Display orders."""

    return render_template(
        'order_summary.html',
        orders=get_orders()
    )
