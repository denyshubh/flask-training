from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import db

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = db.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Create databases, if databases exists doesn't issue create
# For schema changes, run "flask db migrate"
from models import Customer, Account, Transaction
db.create_all()
db.session.commit()

# Verify Using the below command
# psql -h postgres.cluster-cm4hfr3bgsvb.us-east-1.rds.amazonaws.com -p 5432 -d postgres -U postgres -W
# /dt

@app.route('/')
def homepage():
    return render_template('index.html')
