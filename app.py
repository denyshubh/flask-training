from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='static')

POSTGRES_URL= '127.0.0.1:5432'
POSTGRES_USER= 'postgres'
POSTGRES_PW = 'dbpw'
POSTGRES_DB = 'test'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
DEBUG = True

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create databases, if databases exists doesn't issue create
# For schema changes, run "flask db migrate"
from models import Customer, Account, Transaction
db.create_all()
db.session.commit()


@app.route('/')
def homepage():
    return render_template('index.html')
