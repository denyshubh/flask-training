from flask import Flask
from flask_bcrypt import Bcrypt
import config
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(config)
CORS(app)
bcrypt = Bcrypt(app)


def run():
    from app.controller.ers_reimbursement_controller import reimb
    from app.controller.ers_users_controller import er
    app.register_blueprint(er)
    app.register_blueprint(reimb)
    app.run(host="0.0.0.0", port=8080, debug=True)

