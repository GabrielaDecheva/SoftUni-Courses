import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyLowerCase(Exception):
    pass


class NameTooLongError(Exception):
    pass


class WhiteSpaseError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_SYMBOLS_COUNT = 5
MAX_SYMBOLS_COUNT = 20

pattern_lower_case = r"[A-Z]+"
pattern_whitespace = r"\s"

email = input()

while email != "End":
    if len(email.split("@")[0]) < MIN_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")
    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    if re.findall(pattern_lower_case, email):
        raise MustContainOnlyLowerCase("Name must contain only lower case letters!")
    if len(email.split("@")[0]) > MAX_SYMBOLS_COUNT:
        raise NameTooLongError("Name must not be more than 20 characters!")
    if re.findall(pattern_whitespace, email):
        raise WhiteSpaseError("Email must not contain any whitespace!")

    print("Email is valid")

    email = input()
