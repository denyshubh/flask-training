import psycopg

from model.ers_users import Ers_user


class Ers_UserDao:

    def get_user_by_username_and_password(self, username, password):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from registration.users WHERE username = %s AND password = %s", (username, password))

                ers_user_info = cur.fetchone()

                if ers_user_info is None:
                    return None

                username = ers_user_info[0]
                password = ers_user_info[1]
                first_name = ers_user_info[2]
                last_name = ers_user_info[3]
                gender = ers_user_info[4]
                phone_number = ers_user_info[5]
                email_address = ers_user_info[6]

                return ers_user_info(username, password, first_name, last_name, gender, phone_number, email_address)

    def get_user_by_email(self, email):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * from registration.users WHERE email_address = %s", (email,))

                ers_user_info = cur.fetchone()

                if ers_user_info is None:
                    return None

                username = ers_user_info[0]
                password = ers_user_info[1]
                first_name = ers_user_info[2]
                last_name = ers_user_info[3]
                gender = ers_user_info[4]
                phone_number = ers_user_info[5]
                email_address = ers_user_info[6]

                return ers_user_info(username, password, first_name, last_name, gender, phone_number, email_address)

    def get_user_by_username(self, username):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM registration.users WHERE username = %s", (username,))

                ers_user_info = cur.fetchone()

                if ers_user_info is None:
                    return None

                username = ers_user_info[0]
                password = ers_user_info[1]
                first_name = ers_user_info[2]
                last_name = ers_user_info[3]
                gender = ers_user_info[4]
                phone_number = ers_user_info[5]
                email_address = ers_user_info[6]

                return ers_user_info(username, password, first_name, last_name, gender, phone_number, email_address)

    def add_user(self, ers_user_obj):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="zxcvbnm") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO registration.users VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *",
                            (ers_user_obj.username,
                             ers_user_obj.password,
                             ers_user_obj.first_name,
                             ers_user_obj.last_name,
                             ers_user_obj.gender,
                             ers_user_obj.phone_number,
                             ers_user_obj.email_address))

                user_that_was_inserted = cur.fetchone()
                conn.commit()

                return ers_user_obj(user_that_was_inserted[0], user_that_was_inserted[1], user_that_was_inserted[2]
                            , user_that_was_inserted[3], user_that_was_inserted[4], user_that_was_inserted[5]
                            , user_that_was_inserted[6])