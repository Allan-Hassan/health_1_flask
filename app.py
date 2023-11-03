from flask import Flask, url_for, redirect, request, render_template
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
# from flask_sqlalchemy import SQLAlchemy
import os
from classes.models import Category, db

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

if __name__ == '__main__':
    app.run(debug = True)