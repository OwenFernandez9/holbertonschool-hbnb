from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.user import UserRepository
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.amenity_repo = SQLAlchemyRepository(Amenity)
        self.place_repo = SQLAlchemyRepository(Place)
        self.review_repo = SQLAlchemyRepository(Review)

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email) 
       
    def update_user(self, user_id, user_data):
        verify_id = self.user_repo.get(user_id)
        if not verify_id:
            return None
        user_update = self.user_repo.update(user_data)
        return user_update
        
    
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)
    
    def get_amenity_by_name(self, amenity_name):
        return self.amenity_repo.get_by_attribute("name", amenity_name)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        verify_id = self.amenity_repo.get(amenity_id)
        if not verify_id:
            return None
        amenity_update = self.amenity_repo.update(amenity_data)
        return amenity_update

    def create_place(self, place_data):
        place = Place(**place_data)
        self.amenity_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        verify_id = self.place_repo.get(place_id)
        if not verify_id:
            return None
        place_update = self.place_repo.update(place_data)
        return place_update
    
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        all_reviews = self.review_repo.get_all()
        place_reviews = []
        for review in all_reviews:
            if review.place.id == place_id:
                place_reviews.append(review)

        return place_reviews

    def update_review(self, review_id, review_data):
        verify_id = self.review_repo.get(review_id)
        if not verify_id:
            return None
        review_update = self.review_repo.update(review_data)
        return review_update

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        self.review_repo.delete(review_id)
