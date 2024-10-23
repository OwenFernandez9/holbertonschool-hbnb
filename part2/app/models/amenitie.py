import uuid
from datetime import datetime


class Amenity:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = self.validate_name(name)
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    @staticmethod
    def validate_name(name: str) -> str:
        if len(name) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        return name

    def update(self, name: str):
        self.name = self.validate_name(name)
        self.update_at = datetime.now()
