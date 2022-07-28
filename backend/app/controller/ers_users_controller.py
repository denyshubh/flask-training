from flask import Blueprint, request, session, make_response, jsonify
from app.service.ers_users_service import Ers_UserService
from app import bcrypt
import json
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity,jwt_required


er = Blueprint("ers_user_controller", __name__)
Ers_userService = Ers_UserService()

@er.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(hour=1))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

@er.route('/')
def index():
    return render_template('login.html')

@er.route('/login', methods=['POST'])
def login():
    request_body_dict = request.get_json()  # data entered by user
    username = request_body_dict['username']
    pwd = request_body_dict['password']
    # registser -- password inserted to database
    # login -- you enter your password and this password is cross checked with the password already stored in database.
    # If they match then successfull login else invalid credential enterred by user
    try:
        # fetch the user data
        user = Ers_userService.get_user_by_username(username)  # fetching user details from database
        if user and bcrypt.check_password_hash(
                user.password,   # this password we are getting from database
                pwd  # This password is entered by user
        ):
            auth_token = create_access_token(identity=[user.user_id, user.role])  # jason web token
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token
                }
                return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Invalid username or password'
            }
            return make_response(jsonify(responseObject)), 401
    except Exception as e:
        print(e)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 500


@er.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response, 201
    

@er.route('/ers_users', methods=['POST'])
def add_ers_user():
    # register's a user in our database
    ers_user_obj = request.get_json()
    # check if user already exists
    user = Ers_userService.get_user_by_id(ers_user_obj.get('user_id'))  # either None ot ErsUser object
    if not user:
        try:
            user = Ers_userService.add_user(ers_user_obj)  # either None ot ErsUser object
            # generate the auth token
            auth_token = user.encode_auth_token(user.user_id, user.role)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return make_response(jsonify(responseObject)), 202


@er.route('/ers_users/<string:user_id>', methods=['GET'])
@jwt_required()
def get_ers_user(user_id):
    user = Ers_userService.get_user_by_id(user_id)
    if user:
        return user.to_dict(), 201
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User does not exists. Please Register.',
        }
        return make_response(jsonify(responseObject)), 202
