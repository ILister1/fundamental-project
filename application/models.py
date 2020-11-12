# import the db module through which models are assigned

from application import db

# Declare simple tables for MVP

class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(30), nullable=False)

class Venues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(255), nullable=False)
    venue_loc = db.Column(db.String(255), nullable=False)


