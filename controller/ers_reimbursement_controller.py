from flask import Blueprint, request, session,  make_response, jsonify
from service.ers_reimbursement_service import Ers_ReimburseService
from model.ers_users import ErsUser

er = Blueprint("ers_user_controller", __name__)
reimb_service = Ers_ReimburseService()

user_logged_in = True if session.get('auth_token') else False
user_id, role = ErsUser.decode_auth_token(session.get('auth_token'))


@er.route('/reimburse', methods=['GET'])
def get_reimb():
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@er.route('/reimburse', methods=['POST'])
def add_reimb():
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@er.route('/ers_user/<string:ers_user_id>/reimburse', methods=['GET'])
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


@er.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id', methods=['GET'])
def get_reimb_by_reimb_id(reimb_id):
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@er.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id', methods=['PULL'])
def update_reimb_by_reimb_id():
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202


@er.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id', methods=['DELETE'])
def delete_reimb_by_reimb_id():
    if user_logged_in:
        pass
    else:
        responseObject = {
            'status': 'success',
            'message': 'User not logged in. Please login',
        }
        return make_response(jsonify(responseObject)), 202