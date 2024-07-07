from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from models import User
from forms import LoginForm
from models import Contact, db
from forms import ContactForm
import flash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        telefono = form.telefono.data
        mensaje = form.mensaje.data

        nuevo_contacto = Contact(nombre=nombre, apellido=apellido, email=email, telefono=telefono, mensaje=mensaje)
        db.session.add(nuevo_contacto)
        db.session.commit()

        flash('¡Gracias por contactarnos! Te responderemos pronto.', 'success')
        return redirect(url_for('main.home'))

    return render_template('index.html', form=form)

@main.route('/sobremi')
def about():
    return render_template('about.html')

@main.route('/servicios')
def services():
    return render_template('services.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.index'))
    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
