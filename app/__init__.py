from flask import Flask
from flask_bcrypt import Bcrypt

import config
from app.controller.ers_reimbursement_controller import reimb
from app.controller.ers_users_controller import er
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    app.register_blueprint(er)
    app.register_blueprint(reimb)
    app.run(host="0.0.0.0", port=8080, debug=True)

    return app
