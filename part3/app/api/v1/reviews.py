from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource, fields
from app.services import facade


api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})


@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new review"""
        review_data = api.payload
        
        current_user = get_jwt_identity()
        place = facade.get_place(review_data['place_id'])
        if place['owner_id'] == current_user['user_id']:
            return {'error': 'You cannot review your own place.'}, 403
        
        review_existing = facade.get_reviews_by_place(review_data['place_id'])
        for review in review_existing:
            if review.user.id == current_user['id']:        
        #if current_user['user_id']:
                return {'error': 'You have already reviewed this place.'}, 400
        user = facade.get_user(review_data['user_id'])
        if not user:
            return {'error': 'User not found'}, 400

        place = facade.get_place(review_data['place_id'])
        if not place:
            return {'error': 'Place not found'}, 400
        new_review = facade.create_review(review_data)
        return {'id': new_review.id,'text': new_review.text,'rating': new_review.rating,'user_id': new_review.user.id,'place_id': new_review.place.id}, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        reviews = facade.get_all_reviews()
        return reviews

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        # Placeholder for the logic to retrieve a review by ID
        review = facade.get_review(review_id)
        if not review:
            return {'error': 'Review not found'}, 404
        return {'id': review.id,'text': review.text,'rating': review.rating,'user_id': review.user.id,'place_id': review.place.id}, 201

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, review_id):
        """Update a review's information"""
        current_user = get_jwt_identity()
        user = facade.get_user('user_id')
        if user != current_user:
            return {'error': 'Unauthorized action'}, 403
        review = facade.update_user(review_id, api.payload)
        if not review:
            return {"error": "Is not Review"}, 404
        return {'id': review.id,'text': review.text,'rating': review.rating,'user_id': review.user.id,'place_id': review.place.id}, 201

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        current_user = get_jwt_identity()
        user = facade.get_user('user_id')
        if user != current_user:
            return {'error': 'Unauthorized action'}, 403
        del_review = facade.delete_review(review_id)
        if del_review is None:
            return {'error': 'Review not found'}, 404
        return {'message': 'Review deleted successfully'}, 201

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
        @api.response(200, 'List of reviews for the place retrieved successfully')
        @api.response(404, 'Place not found')
        def get(self, place_id):
            """Get all reviews for a specific place"""
            reviews = facade.get_reviews_by_place(place_id)
            if not reviews:
                return {'error':'there is no review'}
            return reviews
