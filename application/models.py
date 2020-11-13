# import the db module through which models are assigned

from application import db

# Declare simple tables for MVP v1.0.0
# Declare one-to-many relationship between bands and venues v11.0.2

class Bands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

class Venues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(255), nullable=False)
    venue_loc = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.String(255), nullable=False)
    entry_fee = db.Column(db.String(255), nullable=False)
    bands = db.relationship('Bands', backref='venue')





