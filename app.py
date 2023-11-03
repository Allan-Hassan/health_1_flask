from flask import Flask, url_for, redirect, request, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categories')
def show_categories():
    return render_template('categories.html')

if __name__ == '__main__':
    app.run(debug = True)