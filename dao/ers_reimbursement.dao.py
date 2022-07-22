import psycopg
from datetime import date
from model.ers_reimbursement import ErsReimburse


class ErsReimbDao:

    def get_ers_user_reimb(self, user_id):
        command = "select * from ERS_REIMBURSEMENT WHERE user_id=(%s);"
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [user_id], binary=True)
                    data = cur.fetchall()  # fetching all rows from customer's table
                    body = []
                    for account in data:
                        body.append(ErsReimburse(*account))
                    if body:
                        return body
        except Exception as e:
            print(e)
        return None

    def get_reimb(self, status):
        command = f"select * from ERS_REIMBURSEMENT WHERE status = (pending, approved, denied)"
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
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
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
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

    def insert_reimb(self, user_id, ers_reimbursement):
        command = (
            '''
            insert into ers_reimbursement(submitted, resolved, description, status, receipt, type, user_id) 
            VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING *;
            '''
        )
        try:
            with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (
                        date.today(),
                        date.today(),
                        ers_reimbursement.get('description'),
                        ers_reimbursement.get('status'),
                        ers_reimbursement.get('receipt'),
                        ers_reimbursement.get('type'),
                        user_id
                    ))
                    conn.commit()
                    inserted_row = cur.fetchone()
                    return ErsReimburse(*inserted_row)

        except Exception as e:
            print(e)

        return None