### Working with virtual environments
To install virtualenv package on your system

```bash
pip install virtualenv
``` 

To create a virtual environment named venv inside your project directory

```bash
virtualenv venv
``` 

To activate the virtual environment

```bash
venv\scripts\activate
```

To install all the dependencies

```bash
pip install -r requirements.txt
```

To deactivate the virtual environment

```bash
venv\scripts\deactivate
```

To update the requirements.txt file

```bash
pip freeze > requirements.txt
```

### Working with databases (mysql)
In this project, i have used the module flask_sqlalchemy to work with databases. This module supports many databases like mysql, postgresql, sqlite, etc.
Using this module, i am able to create classes that represent tables in the database (like other ORM modules, Eloquent for example).

To start using this module, you need to install it using the following command

```bash
pip install Flask-SQLAlchemy
```

You might think that we are going to import the module inside our app.py file, but that's not the case. We are going to create a separate file that will contain all the database related code. This file will be called models.py. And inside this file, we are going to import the module and use it to create our classes.

models.py

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)
```

Meanwhile, inside the app.py file, we are going to import the db object from the models.py file and initialize it.

app.py

```python
from classes.models import Category, db

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
db.init_app(app)
```

#### Example of retrieving data from the database
app.py

```python
@app.route('/categories')
def show_categories():
    categories = Category.query.all()
    return render_template('categories.html', categories = categories)
```

### Migrations
To create a migration folder, run the following command

```bash
flask db init
```

To create a migration file, run the following command

```bash
flask db migrate -m "migration message"
```

To apply the migration, run the following command

```bash
flask db upgrade
```

### Work with images
To work with images, we need to install the module Pillow

```bash
pip install Pillow
```

### Work with forms
To work with forms, we need to install the module Flask-WTF

```bash
pip install Flask-WTF
```

### Work with authentication
To work with authentication, we need to install the module Flask-Login

```bash
pip install Flask-Login
```


### pagination example
```pyhton
@app.route('/cats')
def dis_cats():
    connection = connection = sqlite3.connect('databases/testgpt.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM categories')
    cats = cursor.fetchall()
    
    page = request.args.get('page', 1, type=int)
    items_per_page = 4
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    total_pages = (len(cats) + items_per_page + 1) // items_per_page

    cats_to_display = cats[start_index:end_index]

    return render_template('cats.html', cats=cats_to_display, total_pages=total_pages)
```
