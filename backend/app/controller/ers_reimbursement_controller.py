from flask import Blueprint, request, make_response, jsonify
from app.service.ers_reimbursement_service import Ers_ReimburseService
from app import bcrypt
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity,jwt_required, unset_jwt_cookies

reimb = Blueprint("ers_reimburse_controller", __name__)
reimb_service = Ers_ReimburseService()

@reimb.after_request
def refresh_expiring_jwts(response):
    ''''''
    print('Refresh Expiring Token Called')
    try:
        exp_timestamp = get_jwt().get("exp")
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(days = 2))
        if exp_timestamp and target_timestamp > exp_timestamp:
            print(f"Identity: {get_jwt_identity}")
            auth_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if isinstance(data, dict):
                data["auth_token"] = auth_token
                response.data = jsonify(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        print(response)
        return response


@reimb.route('/reimburse', methods=['GET'])
@jwt_required()
def get_reimb():
    user_id, role = get_jwt_identity()
    if role == 'employee':
        # send employee reimbersement data
        reimb_data = get_reimburse_by_id(user_id)
        if reimb_data:
            responseObject = {
                'status': 'success',
                'data': reimb_data,
                'message': 'Success'
            }
            return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'success',
                'message': 'failed to get data'
            }
            return make_response(jsonify(responseObject)), 202
    else:
        # send all employee reimbersement data
        all_reimb_data = reimb_service.get_all_reimburse()
        if all_reimb_data:
            responseObject = {
                'status': 'success',
                'data': all_reimb_data,
                'message': 'Success'
            }
            return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'success',
                'message': 'failed to get data'
            }
            return make_response(jsonify(responseObject)), 202


@reimb.route('/reimburse/insert', methods=['POST'])
# @jwt_required()
def add_reimb():
    request_body_dict = request.get_json()

    try:
        # fetch the user data
        # reimb_author = get_jwt_identity()[0]  # user_id of current user
        reimb_author = 1
        reimb_data = reimb_service.add_reimbursement(request_body_dict, reimb_author)  # fetching user details from database
        if reimb_data is None:
            response_object = {
                'status': 'failed',
                'message': 'Not able to add reimbursement data',
            }
            return make_response(jsonify(response_object)), 204
        else:
            response_object = {
                'status': 'success',
                'message': 'data upload success!',
                'data': reimb_data.to_dict()
            }
            return make_response(jsonify(response_object)), 200
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(response_object)), 500



@reimb.route('/ers_user/<string:ers_user_id>/reimburse', methods=['GET'])
@jwt_required()
def get_reimb_by_user_id(ers_user_id):
    if user_logged_in:
        # only manager can get all data and current user can access only his own data
        if role == 'finance_manager' or ers_user_id == user_id:  # if role is employee ers_user_id == user_id
            reimburse_data = Ers_ReimburseService.get_reimburse_by_id(ers_user_id)   # list of reimburse or None
            if reimburse_data:
                responseObject = {
                    'status': 'success',
                    'body': reimburse_data,
                }
                make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'success',
                    'message': f'No reimbursement done by employee {ers_user_id}',
                }
                make_response(jsonify(responseObject)), 202
        else:
            responseObject = {
                'status': 'success',
                'message': 'Unauthorized User!',
            }
            return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@reimb.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id>', methods=['GET'])
@jwt_required()
def get_reimb_by_reimb_id(ers_user_id, reimb_id):
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@reimb.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id>', methods=['PULL'])
@jwt_required()
def update_reimb_by_reimb_id(ers_user_id, reimb_id):
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@reimb.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id>', methods=['DELETE'])
@jwt_required()
def delete_reimb_by_reimb_id(ers_user_id, reimb_id):
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202