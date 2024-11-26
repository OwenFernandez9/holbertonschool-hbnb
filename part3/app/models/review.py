from app import db
from app.models.baseclass import BaseModel
from sqlalchemy.orm import validates


class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    @validates('text')
    def validate_text(self, key, text: str) -> str:
        if not text:
            raise ValueError("Review text is required.")
        return text

    @staticmethod
    def validate_rating(self, key, rating: int) -> int:
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating
