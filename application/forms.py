# import forms modules

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Bands, Venues

class GigForm(FlaskForm):
    band_name = StringField('Band Name:',
            validators = [
                DataRequired()
                ]
            )
    submit = SubmitField('Gig')

    def validate_task(self, band_name):
        all_bands = Bands.query.all()
        if band_name.data in all_bands:
            raise ValidationError('This band is already gigging')
