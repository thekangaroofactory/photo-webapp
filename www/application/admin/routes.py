
from flask import Blueprint
from flask import current_app
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from application import admin
from application.models import User
from application import db

app = current_app

# Blueprint Configuration
admin_bp = Blueprint('admin_bp', __name__, template_folder='templates')


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin.html')

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.admin


class MyUserView(ModelView):

    def is_accessible(self):
        if current_user.is_authenticated:
            return current_user.admin

    # Override displayed fields
    column_list = ('name', 'email', 'created', 'admin')


# add views
admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Test'))
admin.add_view(MyView(name='Hello 2', endpoint='test2', category='Test'))

# add user view
admin.add_view(MyUserView(User, db.session))
