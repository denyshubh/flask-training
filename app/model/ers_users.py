import jwt
import datetime
from flask_bcrypt import Bcrypt
import config
from app import create_app

bcrypt = Bcrypt(create_app())

app = create_app()


class ErsUser:

    def __init__(self, user_id, username, password, role, first_name, last_name, gender, phone_number, email_address):
        self.user_id = user_id
        self.username = username
        self.password = bcrypt.generate_password_hash(
            password, config.BaseConfig.BCRYPT_LOG_ROUNDS
        ).decode()
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.email_address = email_address

    def to_dict(self):
        return {
            "user id": self.user_id,
            "username": self.username,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "role": self.role,
            "phone_number": self.phone_number,
            "email_address": self.email_address
        }

    def encode_auth_token(self, user_id, role):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id,
                'role': role
            }
            return jwt.encode(
                payload,
                config.BaseConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            print(e)
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, config.BaseConfig.SECRET_KEY)
            return payload.get('sub'), payload.get('role')

        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

