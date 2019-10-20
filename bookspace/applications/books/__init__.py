from flask import Blueprint

bp = Blueprint('books', __name__)

from bookspace.applications.books import routes