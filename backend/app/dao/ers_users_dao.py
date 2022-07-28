import psycopg

from app.model.ers_users import ErsUser

HOST = 'postgres.cluster-cbdtjy2tmxfd.us-east-1.rds.amazonaws.com'
PWD = 'KT3FfmQtHWUIuqOW8bi3'

class Ers_UserDao:

    def get_user_by_username(self, username):
        command = "SELECT * from ERS_Users WHERE username = %s"

        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [username], binary=True)

                    ers_user_info = cur.fetchone()

                    if ers_user_info:
                        body = ErsUser(*ers_user_info)
                        return body

        except Exception as e:
            print(e, 'Connection Issue!!!')
        return None

    def get_user_by_email(self, email):
        command = "SELECT * from ERS_Users WHERE email_address = %s"

        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [email], binary=True)

                    ers_user_info = cur.fetchone()

                    if ers_user_info:
                        body = ErsUser(*ers_user_info)
                        return body

        except Exception as e:
            print(e, 'Connection Issue!!!')
        return None


    def get_user_by_id(self, user_id):
        command = "SELECT * from ERS_Users WHERE user_id = %s"
        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, [user_id], binary=True)
                    ers_user_info = cur.fetchone()

                    if ers_user_info:
                        body = ErsUser(*ers_user_info)
                        return body

        except Exception as e:
            print(e)
        return None


    def add_user(self, ers_user_obj):
        command = (
            "INSERT INTO ERS_Users(username, password, first_name, last_name, gender, role, phone_number, email_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
        )

        try:
            with psycopg.connect(host=HOST, port="5432", dbname="postgres", user="postgres",
                                 password=PWD) as conn:
                with conn.cursor() as cur:
                    cur.execute(command, (
                        ers_user_obj.get('username'),
                        ers_user_obj.get('password'),
                        ers_user_obj.get('first_name'),
                        ers_user_obj.get('last_name'),
                        ers_user_obj.get('gender'),
                        ers_user_obj.get('role'),
                        ers_user_obj.get('phone_number'),
                        ers_user_obj.get('email_address')
                    ))
                    conn.commit()
                    inserted_row = cur.fetchone()
                    if inserted_row:
                        return ErsUser(*inserted_row)  # unpacking # user registered success
        except Exception as e:
            print(e)
        return None # User already exists

    def update_user(self, ers_user_obj):
        # when user wants to change his details
        pass

    def delete_user(self, user_id):
        pass
