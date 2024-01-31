import tkinter as tk
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


class WhiteSpaceError(Exception):
    pass


class EmptyFieldError(Exception):
    pass


def show_result(result):
    result_label.config(text=result)


def validate_email():
    try:
        email = email_entry.get()

        if not email:
            raise EmptyFieldError("Entry field can not be empty!")

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
            raise WhiteSpaceError("Email must not contain any whitespace!")

        result = "Email is valid"
    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError,
            MustContainOnlyLowerCase, NameTooLongError, WhiteSpaceError, EmptyFieldError) as e:
        result = f"Validation Error: {str(e)}"

    show_result(result)


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_SYMBOLS_COUNT = 5
MAX_SYMBOLS_COUNT = 20

pattern_lower_case = r"[A-Z]+"
pattern_whitespace = r"\s"


window = tk.Tk()
window.title("Email Validator App")
window.geometry("500x350")

email_label = tk.Label(window, text="Enter Email:")
email_label.place(x=90, y=30)

email_entry = tk.Entry(window, width=20)
email_entry.place(x=165, y=30)

validate_button = tk.Button(window, text="Validate Email", height=1, command=validate_email)
validate_button.place(x=310, y=25)

result_label = tk.Label(window, text="")
result_label.place(x=100, y=60)


window.mainloop()