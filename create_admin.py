from app import app, db, User

def create_admin():
    with app.app_context():
        db.create_all()
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        admin = User(username=username, password=password)
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully.")

if __name__ == '__main__':
    create_admin()
