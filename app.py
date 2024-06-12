from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobremi')
def about():
    return render_template('about.html')

@app.route('/servicios')
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run()