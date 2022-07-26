from app.dao.ers_reimbursement_dao import ErsReimbDao


class Ers_ReimburseService:

    def __init__(self):
        self.ers_reimb_dao = ErsReimbDao()

    def get_reimburse_by_id(self, ers_user_id):
        reimburse = self.ErsReimbDao.get_reimb_by_id(ers_user_id)  # list of reimburse or None
        if reimburse is None:
            print(f'No reimbursement done by employee {ers_user_id}')
            return None
        return reimburse

    def get_reimburse_by_reimb_id(self, reimb_id, status):
        reimburse = self.ErsReimbDao.get_reimb_by_id(reimb_id, status)  # single reimbursement or None
        if reimburse is None:
            print(f'No reimbursement id found {reimb_id, status}')
            return None
        return reimburse

    def add_reimbursement(self, ers_users_obj, ):

        if self.reimb_validate(reimb_obj):
            add_reimb_obj = self.ers_reimb_dao.add_reimb(reimb_obj)
            return reimb_obj
        else:
            print('Invalid User Data')
            return {'msg': 'Please Enter Valid User Data', 'status': 404}
