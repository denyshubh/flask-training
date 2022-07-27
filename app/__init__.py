from flask import Flask
from flask_bcrypt import Bcrypt
from config import BaseConfig 
from flask_cors import CORS
from flask_login import LoginManager

bcrypt = Bcrypt()
login_manager = LoginManager()
cors = CORS()

def run():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(BaseConfig)
    cors.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    with app.app_context():
        from app.controller.ers_reimbursement_controller import reimb
        from app.controller.ers_users_controller import er
        app.register_blueprint(er)
        app.register_blueprint(reimb)
        app.run(host="0.0.0.0", port=8080, debug=True)

