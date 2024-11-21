import uuid
from datetime import datetime
from app.models.user import User

class Place:
    def __init__(self, title: str, price: float, latitude: float, longitude: float, owner: User, description: str = None):
        self.id = str(uuid.uuid4())
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.latitude = self.validate_latitude(latitude)
        self.longitude = self.validate_longitude(longitude)
        self.owner = self.validate_owner(owner)
        self.created_at = datetime.now
        self.update_at = datetime.now

    @staticmethod
    def validate_title(title: str) -> str:
        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 words.")
        return title

    @staticmethod
    def validate_price(price: float) -> float:
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        return price
    
    @staticmethod
    def validate_latitude(latitude: float) -> float:
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("The latitude range is outside -90.0 and 90.0.")
        return latitude

    @staticmethod
    def validate_longitude(longitude: float) -> float:
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("The longitud range is outside -180.0 and 180.0.")

    @staticmethod
    def validate_owner(owner, User) -> User:
        if not isinstance(owner, User):
            raise ValueError("Owner not exists.")
        return owner

    def update(self, title: str = None, description: str = None, price: float = None, latitude: float = None, longitude: float = None):
        if title:
            self.title = self.validate_title(title)
        if description is not None:
            self.description = description
        if price is not None:
            self.price = self.validate_price(price)
        if latitude is not None:
            self.latitude = self.validate_latitude(latitude)
        if longitude is not None:
            self.longitude = self.validate_longitude(longitude)
        self.update_at = datetime.now()
