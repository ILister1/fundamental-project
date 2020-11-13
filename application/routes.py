# import the necessary information

from application import app, db
from application.models import Bands, Venues
from flask import render_template, url_for, redirect, request
from application.forms import GigForm

# declare first route for index; to display all_bands

@app.route('/', methods=['POST', 'GET'])
def index():
    all_bands = Bands.query.all()
    return render_template('index.html', title="Gig Listings App", all_bands=all_bands)

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = GigForm()
    if form.validate_on_submit():
        gig = Bands(
                band_name = form.band_name.data,
                genre = 'Jazz',
                venue_id = 1
                )
        db.session.add(gig)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', title='Add a new gig', form=form)



# declare simple routes for update and delete
# in update, we simply update the band with id 1 to new name
# in v1.0.2, update is performed with forms
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = GigForm()
    band = Bands.query.get(id)
    if form.validate_on_submit():
        band.band_name = form.band_name.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.band_name.data = band.band_name
    return render_template('update.html', title='Update Gig', form=form)

# and the same to delete the first one (MVP deliverable)

@app.route('/delete/<int:id>')
def delete(id):
    band = Bands.query.get(id)
    db.session.delete(band)
    db.session.commit()
    return redirect(url_for('index'))

