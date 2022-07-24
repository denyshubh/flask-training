from flask import Flask

import config
from controller.ers_users_controller import er
from flask_cors import CORS


if __name__ == "__main__":
    app = Flask(__name__)
    # app.secret_key = 'asdfghjkl123456'  secrets should never be written in source code.
    app.secret_key = config.BaseConfig.SECRET_KEY
    app.config['SESSION_TYPE'] = config.BaseConfig.SESSION_TYPE

    # If you’re using Flask-Bcrypt to hash user passwords, you’ll need to specify the number of “rounds”
    # that the algorithm executes in hashing a password.
    # The more rounds used to hash a password, the longer it’ll take for an attacker to guess a password given the hash.
    # The number of rounds should increase over time as computing power increases
    # Higher value of  app.config['BCRYPT_LOG_ROUNDS'] = 4 will require higher computation (CPU)
    app.config['BCRYPT_LOG_ROUNDS'] = config.BaseConfig.BCRYPT_LOG_ROUNDS
    CORS(app)  # Instructs our webserver to tell browsers that any origin is allowed. By origin we mean the source
    # where the HTML, CSS, and JS are originating from

    # Session(app)

    app.register_blueprint(er)

    app.run(host="0.0.0.0", port=8080, debug=True)
