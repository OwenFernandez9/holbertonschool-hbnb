from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, fields
from app.services import facade


api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new user"""
        current_user = get_jwt_identity()
        user_data = api.payload

        # Simulate email uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400
        
        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
    
    
    def get(self):
        users = facade.get_all_user()
        return users
        #tenes q hacer un return con un bucle...te la tiro guei

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    @api.expect(user_model, validate=True)
    @jwt_required()
    def put(self, user_id):
        current_user = get_jwt_identity()
        
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403   
        
        iduser = facade.get_user(user_id)
        
        data = request.json
        
        if data.get("password"):
            return {"error": "You cannot modify password."}, 400
        
        email = data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400
        
        user = facade.update_user(user_id, api.payload)
        if not user:
            return {"error": "Is not user"}, 404 
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 201
    
    class Prueba(Resource):
        @api.expect(user_model, validate=True)
        @api.response(201, 'User successfully created')
        @api.response(400, 'Email already registred')
        @api.response(400, 'Invalid input data')
        def post(self):
            user_data = request.json
            data = api.payload
            email = user_data.get('email')

            if facade.get_user_by_email(email):
                return {'error': 'Email already registered'}, 400
            
            new_user = facade.create_user(user_data)
            return {'id': new_user.id, 'mensaje': 'registrado con exito papa'}, 201