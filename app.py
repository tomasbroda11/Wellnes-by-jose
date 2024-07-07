from flask import Flask, render_template, redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin.contrib.sqla import ModelView
from models import User, Contact, db  # Importar la instancia 'db' desde models
from routes import main  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jose.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Inicialización de SQLAlchemy con la aplicación Flask
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Definición de vistas personalizadas para Flask-Admin
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))  # Redirigir a la ruta /admin de Flask-Admin
        return redirect(url_for('login'))

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))

admin = Admin(app, index_view=MyAdminIndexView())
admin.add_view(MyModelView(Contact, db.session))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Registrar el blueprint 'main'
app.register_blueprint(main)

if __name__ == '__main__':
    with app.app_context():
        # Crear las tablas en la base de datos
        db.create_all()
    app.run(debug=True)
