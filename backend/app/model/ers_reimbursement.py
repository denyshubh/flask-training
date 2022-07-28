class ErsReimburse:

    def __init__(self, reimb_id, reimb_amount, submitted, resolved, status, type, description, receipt,
                 reimb_author, reimb_resolver):
        self.reimb_id = reimb_id
        self.reimb_amount = reimb_amount
        self.submitted = submitted
        self.resolved = resolved
        self.status = status
        self.type = type
        self.description = description
        self.receipt = receipt
        self.reimb_author = reimb_author
        self.reimb_resolver = reimb_resolver

    def to_dict(self):
        '''
        This function is used return dictionary of the reimbursement object
        '''
        return {
            "reimb_id": self.reimb_id,
            "reimb_amount": self.reimb_amount,
            "submitted": self.submitted,
            "resolved": self.resolved,
            "status": self.status,
            "type": self.type,
            "description": self.description,
            "receipt": self.receipt,
            "reimb_author": self.reimb_author,
            "reimb_resolver": self.reimb_resolver
            }
