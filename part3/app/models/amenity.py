from app import db
from datetime import datetime
from sqlalchemy.orm import validates
from .baseclass import BaseModel


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(50), nullable=False)

    @validates("name")
    def validate_name(self, key, name: str) -> str:
        if len(name) > 50:
            raise ValueError("Name cannot exceed 50 characters.")
        return name

    def update(self, name: str):
        self.name = self.validate_name(name)
        self.update_at = datetime.now()
