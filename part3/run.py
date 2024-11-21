from app import create_app
from app.models.user import User
from app.services import facade

app = create_app()

pepito = User("a", "a", "string@gmail.com", "string", True)

facade.user_repo.add(pepito)

if __name__ == '__main__':
    app.run(debug=True)
