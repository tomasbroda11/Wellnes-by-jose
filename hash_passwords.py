from app import db, User
from werkzeug.security import generate_password_hash

def hash_existing_passwords():
    with app.app_context():
        # Obtener todos los usuarios de la base de datos
        users = User.query.all()

        # Iterar sobre cada usuario y hashear su contraseña
        for user in users:
            # Hashear la contraseña si no está ya hasheada (para evitar rehashear)
            if not user.password.startswith('$2b$'):
                hashed_password = generate_password_hash(user.password)
                user.password = hashed_password

        # Confirmar los cambios en la base de datos
        db.session.commit()
        print("Contraseñas hasheadas correctamente.")

if __name__ == '__main__':
    hash_existing_passwords()
