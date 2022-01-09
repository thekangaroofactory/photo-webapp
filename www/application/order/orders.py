import os
from flask import current_app

app = current_app


class Order:

    id = 0
    folder = ''
    files = []

    def __init__(self, id, folder, files):
        self.id = id
        self.folder = folder
        self.files = files


def get_orders():
    """Get all orders"""

    # check directory
    target_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    if os.path.exists(target_path):
        folders = os.listdir(target_path)

    # init list
    orders = []
    id = 1

    for folder in folders:

        files = os.listdir(os.path.join(target_path, folder))
        order = Order(id, folder, files)
        orders.append(order)
        id += 1

    return orders
