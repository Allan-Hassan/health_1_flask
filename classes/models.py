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