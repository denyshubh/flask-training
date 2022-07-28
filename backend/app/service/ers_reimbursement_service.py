from app.dao.ers_reimbursement_dao import ErsReimbDao


class Ers_ReimburseService:

    def __init__(self):
        self.ers_reimb_dao = ErsReimbDao()
    
    def get_all_reimburse(self):
        reimburses = self.ers_reimb_dao.get_all_reimb()  # list of reimburse or None
        data = []
        if reimburses is None:
            print(f'No reimbursement done by any employee')
            return None
        for reimb in reimburses:
            data.append(reimb.to_dict())
        return data

    def get_reimburse_by_id(self, ers_user_id):
        reimburse = self.ers_reimb_dao.get_reimb_by_id(ers_user_id)  # list of reimburse or None
        if reimburse is None:
            print(f'No reimbursement done by employee {ers_user_id}')
            return None
        return reimburse

    def get_reimburse_by_reimb_id(self, reimb_id, status):
        reimburse = self.ers_reimb_dao.get_reimb_by_id(reimb_id, status)  # single reimbursement or None
        if reimburse is None:
            print(f'No reimbursement id found {reimb_id, status}')
            return None
        return reimburse

    def add_reimbursement(self, reimb_obj, reimb_author):
        add_reimb_obj = self.ers_reimb_dao.add_reimbursement(reimb_obj, reimb_author)
        if add_reimb_obj:
            return add_reimb_obj
        else:
            print('Reimbursement Data Not Uploaded')
            return None
