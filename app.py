
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

# Initialize the app
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

# Initialize the app
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')  # Change this in production

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import routes
from routes import *

# Create database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)