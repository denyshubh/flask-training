from flask import Blueprint, request, session

from exception.exception_login import LoginError
from exception.exception_registration import RegistrationError
from model.ers_users import Ers_user
from service.ers_users_service import Ers_userService

er = Blueprint("ers_user_controller", __name__)
user_service = Ers_userService()


@er.route('/login_status', methods=['GET'])
def login_status():
    if session.get('ers_user_info') is not None:
        return {
                   "message": "You are logged in",
                   "logged_in_user": session.get('ers_user_info')
               }, 200
    else:
        return {
                   "message": "You are not logged in"
               }, 200


@er.route('/login', methods=['POST'])
def login():
    request_body_dict = request.get_json()

    username = request_body_dict['username']
    password = request_body_dict['password']

    try:
        ers_user_dict = Ers_userService.login(username, password)

        session['ers_user_info'] = ers_user_dict

        return ers_user_dict, 200
    except LoginError as e:
        return {
                   "message": str(e)
               }, 400


@er.route('/logout', methods=['POST'])
def logout():
    session.clear()

    return {
               "message": "Successfully logged out"
           }, 200


@er.route('/ers_users', methods=['POST'])
def add_ers_user():
    request_body_dict = request.get_json()

    username = request_body_dict.get('username')
    password = request_body_dict.get('password')
    first_name = request_body_dict.get('first_name')
    last_name = request_body_dict.get('last_name')
    gender = request_body_dict.get('gender')
    role = request_body_dict.get('role')
    phone_number = request_body_dict.get('phone_number')
    email_address = request_body_dict.get('email_address')

    try:
        added_ers_user = user_service.add_user(Ers_userService(username, password, first_name, last_name, gender, phone_number,
                                                        email_address))
    except RegistrationError as e:
        return {
                   "messages": e.messages
               }, 400

    return added_ers_user, 201


@er.route('/ers_users/<string:user_id>', methods=['GET'])
def get_ers_user(user_id):
    if Ers_userService.get_user_by_id(user_id):
        return "Users info"

    else:
        return {
                   "message": "Not a valid user"
               }, 200