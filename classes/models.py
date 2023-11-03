from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    picture = db.Column(db.String(100), nullable = False)

    def __repr__(self): # This method is for debugging purposes
        return f"Category('{self.name}', '{self.picture}')"