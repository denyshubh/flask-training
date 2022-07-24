from dao.ers_reimbursement_dao import ErsReimbDao


class Ers_ReimburseService:

    def __init__(self):
        self.ers_reimb_dao = ErsReimbDao()

    def get_reimburse_by_id(self, ers_user_id):
        reimburse = self.ErsReimbDao.get_reimb_by_id(ers_user_id)  # list of reimburse or None
        if reimburse is None:
            print(f'No reimbursement done by employee {ers_user_id}')
            return None
        return reimburse
