# import the basic requirements for Flask, SQL and environment variables for stability and security

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

# Declare the app object

app = Flask(__name__)

# Declare the configuration for secure environment variables

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# Declare the db object as an argument to SQLAlchemy

db = SQLAlchemy(app)

# import the routes

from application import routes
