import sys
import logging

from flask_cors import CORS

from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://tlsrwjhokimtos:5fefa6b78e17bcaf08e3ca9f620e2643b0093f255d470ecb5009519ba14542a6@ec2-54-161-208-31.compute-1.amazonaws.com:5432/dbfdfli3u39h0d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(Config)
CORS(app)
db.init_app(app)
migrate.init_app(app, db)
api = Api(app)
mail = Mail(app)

from bookspace.applications.users import bp as users_bp

app.register_blueprint(users_bp)

from bookspace.applications.books import bp as books_bp

app.register_blueprint(books_bp)

app.app_context().push()
db.create_all(app=app)

session = db.session()


######## DO NOT DELETE  ###########

# @app.route('/add')
# def import_books():
#     file = open("/home/d/files/prp/books_cleared.csv")
#     reader = csv.reader(file)
#     for id, title, author, genre, pages in reader:
#         session.execute("""INSERT INTO Books (id, title, author, genre, pages, rate)
#         VALUES (:id, :title, :author, :genre, :pages, :rate)""", {'id': id, 'title': title,
#         'author': author, 'genre': genre, 'pages': pages, 'rate': 0})
#     session.commit()
#     return 'ok'


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
