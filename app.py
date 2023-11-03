from flask import Flask, url_for, redirect, request, render_template
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy
import os
from classes.models import Category, Product, db

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
    # username = request.form['username']
    # password = request.form['password']
    # if username == 'admin' and password == 'admin':
    #     return redirect(url_for('home'))
    # else:
    #     return redirect(url_for('show_login_page'))
    pass
@app.route('/register')
def show_register_page():
    return render_template('auth/guest/register.html')
if __name__ == '__main__':
    app.run(debug = True)