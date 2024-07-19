from app import app, db, User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        db.create_all()
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        # Hashear la contraseña antes de guardarla en la base de datos
        hashed_password = generate_password_hash(password)

        admin = User(username=username, password=hashed_password)
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully.")


if __name__ == '__main__':
    create_admin()
