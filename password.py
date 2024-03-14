# 2. Create a class that securely stores and manages passwords.
# Use properties with getters and setters to ensure password security and prevent unauthorized access.

# Requirements:
#  - Define a property named password that sets the password. The setter should:
#  - Enforce a minimum password length (e.g., 8 characters).
#  - Check for common password patterns or dictionary words (optional for an extra challenge).
#  - Hash the password using a secure hashing algorithm (e.g., SHA-256) before storing it.
#  - Create a getter for password that always returns randomly placed 8 to 12 elements from hash function  (symbols must not be duplicated) to prevent direct access to the actual password.
#  - Create a setter, that would take current password and new one, if current password is correct , would set new one, otherwise raise error.

import hashlib, random
from dataclasses import dataclass
from typing import Callable


@dataclass
class NewPassword:
    old_password: str
    new_password: str


class WrongPasswordError(Exception):
    pass


class Password:
    MIN_PASSWORD_LENGTH = 6
    WEAK_PASSWORDS = [
        "123456",
        "12345678",
        "123456789",
        "12345",
        "1234567",
        "password",
        "abcdef",
        "abc123",
        "qwerty",
        "111111",
        "1234",
        "iloveyou",
    ]

    def __init__(self, password: str) -> None:
        self._password = self._validate_password(password)

    def _validate_password(self, password) -> str:
        if (
            len(password) >= self.MIN_PASSWORD_LENGTH
            and password not in self.WEAK_PASSWORDS
        ):
            print("Password meets the requirements.")
            hashed_password = self._hash_password(password=password)
            return hashed_password
        else:
            return "Weak password"

    @staticmethod
    def _hash_password(password) -> str:
        password_bytes = password.encode("utf-8")
        hash_object = hashlib.sha256(password_bytes)
        return hash_object.hexdigest()

    def get_scrambled_hash(self) -> str:
        hash_list = []
        while len(hash_list) < random.randint(8, 12):
            x = self._password[random.randrange(64)]
            if x not in hash_list:
                hash_list.append(x)
        scrambled_hash = "".join(hash_list)
        return scrambled_hash

    @property
    def password(self) -> str:
        return self.get_scrambled_hash()

    @password.setter
    def password(self, new_password: "NewPassword") -> None:
        compare_hash = self._hash_password(password=new_password.old_password)
        if compare_hash == self._password:
            self._password = self._validate_password(new_password.new_password)
            print("New password has been set")
        else:
            raise WrongPasswordError("Wrong password")


passw = Password("passwordas")

print(passw.password)

new_password = NewPassword(old_password="passwordas", new_password="blablablabal")

try:
    passw.password = new_password
except WrongPasswordError as err:
    print(err)

print(passw.password)
