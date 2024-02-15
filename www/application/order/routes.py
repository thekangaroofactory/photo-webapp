
from flask import Blueprint, current_app
from flask import render_template, send_from_directory
from flask_login import login_required, current_user

from application.order.orders import get_orders
from application.admin.tools import admin_required

import time
from io import BytesIO
import zipfile
import os
from flask import send_file

app = current_app

# Blueprint Configuration
order_bp = Blueprint('order_bp', __name__,
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='/order_bp/static/')


@order_bp.route('/order', methods=['GET'])
@login_required
@admin_required
def show_orders():
    """Display orders."""

    return render_template(
        'order_summary.html',
        orders=get_orders()
    )


@order_bp.route('/get_img/<folder>/<file>', methods=['GET'])
@login_required
@admin_required
def get_img(folder, file):
    return send_from_directory(os.path.join(app.config["UPLOAD_FOLDER"], folder), file)


@app.route('/zipped/<folder>')
def zipped_data(folder):
    time_str = time.strftime("%Y%m%d-%H%M%S")
    file_name = "my_data_dump_{}.zip".format(time_str)
    memory_file = BytesIO()
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], folder)
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                zipf.write(os.path.join(root, file))
    memory_file.seek(0)
    return send_file(memory_file,
                     attachment_filename=file_name,
                     as_attachment=True)
