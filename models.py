from uuid import uuid4
from app import db

class Account(db.Model):
    __tablename__ = 'accounts'
 
    account_id = db.Column(db.String(200), primary_key=True, default=uuid4)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150))
    balance = db.Column(db.Float, nullable=False, default=0)
    credit_line =  db.Column(db.String(50), nullable=False)
    begin_balance =  db.Column(db.Float, nullable=False)
    begin_balance_timestamp = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.String(200), db.ForeignKey('customers.customer_id'), nullable=False)
    
    # def __init__(self, Field1_name,Field1_name,Field1_name):
    #     self.field1_name = field1_name
    #     self.field2_name = field2_name
    #     self.field3_name = field3_name
 
    def __repr__(self):
        return f"Account Create for Customer with ID {self.customer_id}"

class Customer(db.Model):
    __tablename__ = 'customers'
 
    customer_id = db.Column(db.String(200),primary_key=True, default=uuid4)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    middle_initial = db.Column(db.String(1))
    street =  db.Column(db.String(50), nullable=False)
    city =  db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip =  db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(15), nullable=False) 
    email = db.Column(db.String(50), nullable=False)
    accounts = db.relationship('accounts', backref='customers', lazy=True)
    # def __init__(self, Field1_name,Field1_name,Field1_name):
    #     self.field1_name = field1_name
    #     self.field2_name = field2_name
    #     self.field3_name = field3_name
 
    def __repr__(self):
        return f"Account Created For User {self.first_name}, {self.last_name}"

class Transaction(db.Model):
    __tablename__ = 'transactions'
 
    txn_id = db.Column(db.String(200),primary_key=True, default=uuid4)
    balance = db.Column(db.Float, nullable=False, default=0)
    amount =  db.Column(db.Float, nullable=False, default=0)
    timestamp = db.Column(db.DateTime, nullable=False)
    account_id = db.Column(db.String(200), db.ForeignKey('accounts.account_id'), nullable=False)
 
    # def __init__(self, Field1_name,Field1_name,Field1_name):
    #     self.field1_name = field1_name
    #     self.field2_name = field2_name
    #     self.field3_name = field3_name
 
    def __repr__(self):
        return f"Transaction made of amount {self.amount}. Remaining balance is {self.balance}"
