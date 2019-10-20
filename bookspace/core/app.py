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
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://orwmtckfmaantv:9d4f5b41163eb99a0b92f6a983010c41fc3f89806f43087b9381d23481cbdd31@ec2-23-21-129-125.compute-1.amazonaws.com:5432/d9c2d2fn6ej2d2'
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
