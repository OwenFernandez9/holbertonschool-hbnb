from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.persistence.repository import AmenityRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)
    
    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity task 3
        if 'name' not in amenity_data or not amenity_data['name']:
            raise ValueError('The name not exists')
        """
        new_amenity = (name=amenity_data['name'])
        save = self.amenity_repo.save(new_amenity)
        return {
            "id": save.id,
            "name": save.name
        }
        """
        pass
        

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID task 3
        pass

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities task 3
        pass

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity task 3 PUT
        pass

    def create_place(self, place_data):
        # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        pass

    def get_place(self, place_id):
        # Placeholder for logic to retrieve a place by ID, including associated owner and amenities
        pass

    def get_all_places(self):
        # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        # Placeholder for logic to update a place
        pass
