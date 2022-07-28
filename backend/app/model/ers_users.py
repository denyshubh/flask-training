import jwt
import datetime
import config
from app import bcrypt


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