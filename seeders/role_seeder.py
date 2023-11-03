import os
import sys

# Get the directory of the current script (role_seeder.py)
current_dir = os.path.dirname(os.path.realpath(__file__ ))

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from app import app
from classes.models import db, Role, Category, Product

def seed_roles():
    with app.app_context():
        # First, clear the existing data by dropping the table.
        db.session.query(Role).delete()
        
        seed_data = [
            Role(id=1,title='admin', level=1),
            Role(id=2,title='user', level=3),
            Role(id=3,title='guest', level=5),
        ]

        for data in seed_data:
            db.session.add(data)
        db.session.commit()

if __name__ == "__main__":
    seed_roles()