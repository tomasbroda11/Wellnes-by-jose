from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from models import User, Contact, db
from forms import LoginForm, ContactForm
from werkzeug.security import check_password_hash
from flask_mail import Message
from config import mail

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
        
        # Guardar en la base de datos
        nuevo_contacto = Contact(nombre=nombre, apellido=apellido, email=email, telefono=telefono, mensaje=mensaje)
        db.session.add(nuevo_contacto)
        db.session.commit()

        # Enviar correo electrónico
        msg = Message('Nuevo mensaje de contacto', 
                      recipients=['tomasbroda13@gmail.com'])  # Cambia esto por tu dirección de correo
        msg.body = f"""
        Nuevo mensaje de contacto desde la web.
        Nombre: {nombre}
        Apellido: {apellido}
        Email: {email}
        Teléfono: {telefono}
        Mensaje: {mensaje}
        """

        try:
            mail.send(msg)
            flash('¡Gracias por contactarnos! Te responderemos pronto.', 'success')
        except Exception as e:
            flash(f'Ocurrió un error al enviar el mensaje', 'danger')
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
        if user and check_password_hash(user.password, form.password.data):  # Usa check_password_hash para mayor seguridad
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('admin.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
