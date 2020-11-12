# import the necessary information

from application import app, db
from application.models import Bands
from flask import render_template

# declare first route for index; to display all_bands

@app.route('/')
def index():
    all_bands = Bands.query.all()
    return render_template('index.html', all_bands=all_bands)

@app.route('/add')
def add():
    latest_band = Bands.query.order_by(Bands.id.desc()).first()
    if latest_band:
        new_band = Bands(band_name="New Band"+str(latest_band.id + 1),genre ='Alternative')
    else:
        new_band = Bands(band_name="New Band1", genre ='Disco')
    db.session.add(new_band)
    db.session.commit()
    return "Added a new band"


# declare simple routes for update and delete
# in update, we simply update the band with id 1 to new name
@app.route('/update/<band_name>',methods=['POST'])
def update(band_name):
    latest_band = Bands.query.order_by(Bands.id.desc()).first()
    latest_band.band_name = band_name
    db.session.commit()
    return "Updated the first band name"

# and the same to delete the first one (MVP deliverable)

@app.route('/delete',methods=['POST'])
def delete():
    latest_band = Bands.query.order_by(Bands.id.desc()).first()
    db.session.delete(latest_band)
    db.session.commit()
    return "Deleted most recently added band"

