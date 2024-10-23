import uuid
from datetime import datetime
from place import Place
from user import User



class Review:
    def __inti__(self, text: str, rating: int, place: Place, user: User):
        self.id = id
        self.text = self.validate_text(text)
        self.rating = self.validate_rating(rating)
        self.place = self.validate_place(place)
        self.user = self.validate_user(user)
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    @staticmethod
    def validate_text(text: str) -> str:
        if not text:
            raise ValueError("Review text is required.")
        return text

    @staticmethod
    def validate_rating(rating: int) -> int:
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        return rating
    
    @staticmethod
    def validate_place(place: Place) -> Place:
        if not isinstance(place, Place):
            raise ValueError("Place must be validated")
        return place

    @staticmethod
    def validate_user(user: User) -> User:
        if not isinstance(user, User):
            raise ValueError("User must be validate")
        return user

    def update(self, text: str = None, rating: int = None):
        if text:
            self.text = self.validate_text(text)
        if rating is not None:
            self.rating = self.validate_rating(rating)
        self.update_at = datetime.now()