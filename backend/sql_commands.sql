CREATE TABLE ERS_Users (
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(255) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	role text NOT NULL CHECK( role in ('finance_manager','employee')),
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	gender VARCHAR(20) NOT NULL,
	phone_number VARCHAR (12) NOT null CHECK(phone_number SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
    email_address VARCHAR (255) unique NOT null check (email_address like '%_@__%.__%')

);

CREATE TABLE ERS_REIMBURSEMENT (
    reimb_id SERIAL PRIMARY KEY,
	reimbursement_amount NUMERIC NOT NULL,
	submitted TIMESTAMP(20) NOT NULL,
	resolved TIMESTAMP(30),
	status text NOT NULL CHECK( status in ('pending','approved','denied')),
	type text NOT NULL CHECK(type in ('Lodging','Travel','Food','Other')),
	description VARCHAR(100) NOT NULL,
	receipt text NOT NULL,
	reimb_author SERIAL NOT NULL,
    reimb_resolver SERIAL,
	CONSTRAINT fk_reimb_author FOREIGN KEY(reimb_author) REFERENCES ERS_Users(user_id),
	CONSTRAINT fk_reimb_resolver FOREIGN KEY(reimb_resolver) REFERENCES ERS_Users(user_id)
);