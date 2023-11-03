from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    picture = db.Column(db.String(100), nullable = False)

    def __repr__(self): # This method is for debugging purposes
        return f"Category('{self.name}', '{self.picture}')"
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    picture = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    category = db.relationship('Category', backref = db.backref('products', lazy = True))

    def __repr__(self): # This method is for debugging purposes
        return f"Product('{self.name}', '{self.picture}', '{self.description}', '{self.price}', '{self.category_id}')"    
    
class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    level = db.Column(db.Integer, nullable = False)

    def __repr__(self): # This method is for debugging purposes
        return f"Role('{self.name}')"
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable = False)
    role = db.relationship('Role', backref = db.backref('users', lazy = True))

    def __repr__(self): # This method is for debugging purposes
        return f"User('{self.name}', '{self.email}', '{self.password}', '{self.role_id}')"    