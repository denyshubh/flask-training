CREATE TABLE ERS_Users (
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	password VARCHAR(500) NOT NULL,
	role text NOT NULL CHECK( role in ('finance_manager','employee')),
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	gender VARCHAR(20) NOT NULL,
	phone_number VARCHAR (12) NOT null CHECK(phone SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
    email_address VARCHAR (50) unique NOT null check (email like '%_@__%.__%')

);

CREATE TABLE ERS_REIMBURSEMENT (
    reimb_id SERIAL PRIMARY KEY,
	reimbursement_amount NUMERIC NOT NULL,
	submitted TIMESTAMP(20) NOT NULL,
	resolved TIMESTAMP(30) NOT NULL,
	status text NOT NULL CHECK( status in ('pending','approved','denied')),
	type text NOT NULL CHECK(type in ('Lodging','Travel','Food','Other')),
	description VARCHAR(100) NOT NULL,
	receipt BYTEA NOT NULL,
	reimb_author SERIAL,
    reimb_resolver SERIAL,
	CONSTRAINT fk_reimb_author FOREIGN KEY(reimb_author) REFERENCES ERS_Users(user_id),
	CONSTRAINT fk_reimb_resolver FOREIGN KEY(reimb_resolver) REFERENCES ERS_Users(user_id)
);