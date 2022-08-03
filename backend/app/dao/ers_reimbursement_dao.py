import psycopg
from datetime import date
from app.model.ers_reimbursement import ErsReimburse
import config
HOST = config.BaseConfig.DB_HOST
PWD = config.BaseConfig.DB_PWD

class ErsReimbDao:

    def get_reimb_by_id(self, user_id):
        command = "select * from ERS_REIMBURSEMENT WHERE user_id=(%s);"
        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [user_id], binary=True)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for reimburse in data:
                        body.append(ErsReimburse(*reimburse))
                    if body:
                        return body
        except Exception as e:
            print(e)
        return None

    def get_all_reimb(self):
        command = "select * from ERS_REIMBURSEMENT;"
        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, binary=True)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for reimburse in data:
                        body.append(ErsReimburse(*reimburse))
                    if body:
                        return body
        except Exception as e:
            print(e)
        return None


    def get_reimb(self, status):
        command = f"select * from ERS_REIMBURSEMENT WHERE status = (pending, approved, denied)"
        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [status], binary=True)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for account in data:
                        body.append(ErsReimburse(*account))
                    if body:
                        return body
        except Exception as e:
            print(e)
        return None

    def get_reimb_by_reimb_id(self, reimb_id):
        command = "select * from ERS_REIMBURSEMENT WHERE reimb_id=(%s);"
        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [reimb_id], binary=True)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for account in data:
                        body.append(ErsReimburse(*account))
                    if body:
                        return body
        except Exception as e:
            print(e)
        return None

    def add_reimbursement(self, reimb_data, reimb_author):
        
        command = (
            '''
            insert into ers_reimbursement(reimbursement_amount, submitted, resolved, description, status, receipt, type, reimb_author, reimb_resolver) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *;
            '''
        )
        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    if reimb_data.get('status') != 'pending':
                        cur.execute(command, (
                            reimb_data.get('reimbursement_amount'),
                            date.today(),
                            date.today(),
                            reimb_data.get('description'),
                            reimb_data.get('status'),
                            reimb_data.get('receipt'),
                            reimb_data.get('type'),
                            reimb_author,
                            reimb_author
                        ))
                    else:
                         cur.execute(command, (
                            reimb_data.get('reimbursement_amount'),
                            date.today(),
                            None,
                            reimb_data.get('description'),
                            reimb_data.get('status'),
                            reimb_data.get('receipt'),
                            reimb_data.get('type'),
                            reimb_author,
                            None
                        ))
                    conn.commit()
                    inserted_row = cur.fetchone()
                    if inserted_row:
                        return ErsReimburse(*inserted_row)

        except Exception as e:
            print(e)

        return None