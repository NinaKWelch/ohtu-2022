import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


def check_characters(user_entry):
    # https://stackoverflow.com/questions/3617797/regex-to-match-only-letters
    match = re.findall("[^\W\d_]", user_entry)

    return len(match)


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("Username too short")

        if len(password) < 8:
            raise UserInputError("Password too short")

        if check_characters(username) != len(username):
            raise UserInputError("Username must only contain letters")

        if check_characters(password) == len(password):
           raise UserInputError("Password must contain numbers or special characters")

        if password_confirmation and password != password_confirmation:
            raise UserInputError("Passwords not matching")


user_service = UserService()
