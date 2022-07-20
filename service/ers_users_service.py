import re

from dao.ers_users_dao import Ers_UserDao
from exception.exception_login import LoginError
from exception.exception_registration import RegistrationError


class Ers_userService:
    def __init__(self):
        self.ers_users.dao = Ers_UserDao()

    def login(self, username, password):
        ers_user_obj = self.ers_users_dao.get_ers_user_by_username_and_password(username, password)

        if ers_user_obj is None:
            raise LoginError("Invalid username and/or password")

        return ers_user_obj.to_dict()

    def add_ers_users(self, ers_users_obj):

        registration_error = RegistrationError()

        if not ers_users_obj.username.isalnum():
            registration_error.messages.append("Username must only contain alphanumeric characters")

        if len(ers_users_obj.username) < 6 or len(ers_users_obj.username) > 20:
            registration_error.messages.append("Username must be between 6 and 20 characters in length inclusive")

        if self.ers_users_dao.get_user_by_username(ers_users_obj.username) is not None:
            registration_error.messages.append("Username is already taken")

        if ers_users_obj.username == '':
            registration_error.messages.append("Username must not be blank")

        alphabetical_characters = "abcdefghijklmnopqrstuvwxyz"
        special_characters = "!@#$%^&*"
        numeric_characters = "0123456789"

        lower_alpha_count = 0
        upper_alpha_count = 0
        special_character_count = 0
        numeric_character_count = 0
        for char in ers_users_obj.password:
            if char in alphabetical_characters:
                lower_alpha_count += 1

            if char in alphabetical_characters.upper():
                upper_alpha_count += 1

            if char in special_characters:
                special_character_count += 1

            if char in numeric_characters:
                numeric_character_count += 1

        if lower_alpha_count == 0:
            registration_error.messages.append("Password must have at least 1 lowercase character")

        if upper_alpha_count == 0:
            registration_error.messages.append("Password must have at least 1 uppercase character")

        if special_character_count == 0:
            registration_error.messages.append("Password must have at least 1 special (!@#$%^&*) character")

        if numeric_character_count == 0:
            registration_error.messages.append("Password must have at least 1 numeric character")

        if len(ers_users_obj.password) < 6 or len(ers_users_obj.password) > 20:
            registration_error.messages.append("Password must be between 6 and 20 characters in length inclusive")

        if len(ers_users_obj.password) != lower_alpha_count + upper_alpha_count + special_character_count + numeric_character_count:
            registration_error.messages.append("Password must contain only alphanumeric and special characters")

        # First Name validation
        if not ers_users_obj.first_name.isalpha():
            registration_error.messages.append("First name must contain only alphabetical characters")

        if len(ers_users_obj.first_name) < 2 or len(ers_users_obj.first_name) > 100:
            registration_error.messages.append("Length of first name must be between 2 and 100 characters inclusive")

        if ers_users_obj.first_name == '':
            registration_error.messages.append("First_name must not be blank")

        # Last Name validation
        if not ers_users_obj.last_name.isalpha():
            registration_error.messages.append("Last name must contain only alphabetical characters")

        if len(ers_users_obj.last_name) < 2 or len(ers_users_obj.last_name) > 100:
            registration_error.messages.append("Length of last name must be between 2 and 100 characters inclusive")

        if ers_users_obj.last_name == '':
            registration_error.messages.append("Last_name must not be blank")

        # Gender validation
        if not (ers_users_obj.gender == "male" or ers_users_obj.gender == "female" or ers_users_obj.gender == "other"):
            registration_error.messages.append("Gender must be male, female, or other")

        if ers_users_obj.first_name == '':
            registration_error.messages.append("Gender must be selected")

        # Phone number validation
        if not re.fullmatch("\d{3}-\d{3}-\d{4}", ers_users_obj.phone_number):
            registration_error.messages.append("Phone number must match the format XXX-XXX-XXXX")

        if ers_users_obj.phone_number == '':
            registration_error.messages.append("Phone_number must not be blank")

        # Email address validation
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', ers_users_obj.email_address):
            registration_error.messages.append("Email address must match format username@domain")

        if self.user_dao.get_user_by_email(ers_users_obj.email_address) is not None:
            registration_error.messages.append("Email address is already taken")

        if ers_users_obj.email_address == '':
            registration_error.messages.append("email_address must not be blank")

        # If error messages exist in the exception object, raise the exception
        if len(registration_error.messages) > 0:
            raise registration_error  # Raise will immediately terminate the currently executing function
            # and pass the exception back to the function that called this function

        added_user_obj = self.user_dao.add_user(ers_users_obj)

        return added_user_obj.to_dict()
