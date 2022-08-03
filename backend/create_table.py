import psycopg
import config

def create_table():
    commands = (
        """
        DROP TABLE IF EXISTS ERS_REIMBURSEMENT;
        """,
        """
        DROP TABLE  IF EXISTS ERS_Users;
        """,
        """
        CREATE TABLE ERS_Users (
            user_id text PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            role text NOT NULL CHECK( role in ('finance_manager','employee')),
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            gender VARCHAR(20) NOT NULL,
            phone_number VARCHAR (12) NOT null CHECK(phone_number SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
            email_address VARCHAR (255) unique NOT null check (email_address like '%_@__%.__%')

        );
        """,
        """
        CREATE TABLE ERS_REIMBURSEMENT (
            reimb_id SERIAL PRIMARY KEY,
            reimbursement_amount NUMERIC NOT NULL,
            submitted TIMESTAMP(20) NOT NULL,
            resolved TIMESTAMP(30),
            status text NOT NULL CHECK( status in ('pending','approved','denied')),
            type text NOT NULL CHECK(type in ('Lodging','Travel','Food','Other')),
            description VARCHAR(100) NOT NULL,
            receipt text,
            reimb_author text NOT NULL,
            reimb_resolver text,
            CONSTRAINT fk_reimb_author FOREIGN KEY(reimb_author) REFERENCES ERS_Users(user_id),
            CONSTRAINT fk_reimb_resolver FOREIGN KEY(reimb_resolver) REFERENCES ERS_Users(user_id)
        );
        """
    )
    try:
        with psycopg.connect(host=config.BaseConfig.DB_HOST, port="5432", dbname="postgres", user="postgres",
                                password=config.BaseConfig.DB_PWD) as conn:
              with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command, binary=True)
                print("Success@!")

    except Exception as e:
        print(e)

create_table()