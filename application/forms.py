# import forms modules

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Bands, Venues

class GigForm(FlaskForm):
    band_name = StringField('Band Name: ',
            validators = [
    DataRequired()
                ]
            )
    genre = StringField('Genre: ',
            validators = [
                DataRequired()
                ]
            )
    venue_id = SelectField(u'Choose Venue', choices=[('1', 'The Duchess, York'), ('2', 'Brudenell Social Club, Leeds'),('3', 'Millennium Dome, London')], coerce=int)
    submit = SubmitField('Update Gig')

    def validate_band_name(self, band_name):
        all_bands = Bands.query.all()
        if band_name.data in all_bands:
            raise ValidationError('This band is already gigging')
