import uuid
from datetime import datetime
import re


class User:
    def __init__(self, first_name: str, last_name: str, email: str, is_admin: bool = False):
        self.id = str(uuid.uuid4())
        self.first_name = self.validate_name(first_name)
        self.last_name = self.validate_name(last_name)
        self.email = self.validate_email(email)
        self.is_admin = is_admin
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    @staticmethod
    def validate_name(name: str) -> str:
        if len(name) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        return name

    @staticmethod
    def validate_email(email: str) -> str:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email format.")
        return email

    def update(self, first_name: str = None, last_name: str = None, email: str = None, is_admin: bool = None):
        if first_name:
            self.first_name = self.validate_name(first_name)
        if last_name:
            self.last_name = self.validate_name(last_name)
        if email:
            self.email = self.validate_email(email)
        if is_admin is not None:
            self.is_admin = is_admin
        self.updated_at = datetime.now()
