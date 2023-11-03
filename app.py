from flask import Flask, url_for, redirect, request, render_template
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
from classes.models import Category, Product, db, Role, User

from passlib.hash import sha256_crypt

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categories')
def show_categories():
    categories = Category.query.all()
    return render_template('categories.html', categories = categories)

@app.route('/category/<int:id>')
def show_category(id):
    products = Product.query.filter_by(category_id = id).all()
    category_name = Category.query.filter_by(id = id).first().name
    return render_template('category.html', products = products, category_name = category_name)

@app.route('/login')
def show_login_page():
    return render_template('auth/guest/login.html')

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    pass

@app.route('/register')
def show_register_page():
    return render_template('auth/guest/register.html')

@app.route('/register', methods = ['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    if not name or not email or not password: # Check if the fields are empty
        return redirect(url_for('show_register_page'))
    
    if password != password_confirmation:
        return redirect(url_for('show_register_page'))
    
    user = User.query.filter_by(email = email).first() # Check if the email already exists
    if user:
        return redirect(url_for('show_register_page'))
    hashed_password = sha256_crypt.hash(password) # Hash the password
    new_user = User(name = name, email = email, password = hashed_password, role_id = 3)
    db.session.add(new_user) # Add the new user to the database
    db.session.commit() # Commit the changes
    return redirect(url_for('show_login_page'))
if __name__ == '__main__':
    app.run(debug = True)