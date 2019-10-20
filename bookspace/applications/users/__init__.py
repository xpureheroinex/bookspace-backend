from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/')

from bookspace.applications.users import routes
