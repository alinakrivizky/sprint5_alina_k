from dataclasses import dataclass

BASE_URL = "https://qa-desk.education-services.ru/"
LOGIN_PATH = "/login"

VALID_USER_EMAIL = "al@gmail.com"
VALID_USER_PASSWORD = "aaaaaddddd12R"
INVALID_EMAIL = "invalid-email"
NEW_USER_EMAIL_FORMAT = "user{timestamp}@example.com"

@dataclass(frozen=True)
class RegistrationData:
    valid_email: str = VALID_USER_EMAIL
    password: str = VALID_USER_PASSWORD
    invalid_email: str = INVALID_EMAIL
    new_user_email_format: str = NEW_USER_EMAIL_FORMAT
