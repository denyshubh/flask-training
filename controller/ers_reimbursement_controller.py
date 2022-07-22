from flask import Blueprint, request, session

from exception.exception_registration import RegistrationError
from model.ers_reimbursement import ers_reimb
from service.ers_reimbursement_service import Ers_reimbService

er = Blueprint("ers_user_controller", __name__)
user_service = Ers_reimbService()


@er.route('/reimburse', methods=['GET'])
def get_reimb():
    pass


@er.route('/reimburse', methods=['POST'])
def create_reimb():
    pass


@er.route('/ers_user/<string:ers_user_id>/reimburse', methods=['GET'])
def get_reimb_by_user_id():
    pass


@er.route('/ers_user/<string:ers_user_id>/reimburse/<string:reimb_id', methods=['GET'])
def get_reimb_by_reimb_id():
    pass
