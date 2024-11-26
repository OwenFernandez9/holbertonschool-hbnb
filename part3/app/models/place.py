from app import db
from .baseclass import BaseModel
from sqlalchemy.orm import validates
#from app.models.user import User

class Place(BaseModel):
    __tablename__ = 'places'
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    @validates("title")
    def validate_title(self, key, title: str) -> str:
        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 words.")
        return title

    @validates("price")
    def validate_price(self, key, price: float) -> float:
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        return price
    
    @validates("latitude")
    def validate_latitude(self, key, latitude: float) -> float:
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("The latitude range is outside -90.0 and 90.0.")
        return latitude

    @validates("longitude")
    def validate_longitude(self, key, longitude: float) -> float:
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("The longitud range is outside -180.0 and 180.0.")

     # TODO [fabri] No se si esto lo valida SQLAlchemy...
    #@staticmethod
    #def validate_owner(owner, User) -> User:
    #    if not isinstance(owner, User):
    #        raise ValueError("Owner not exists.")
    #    return owner
