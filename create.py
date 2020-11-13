from application import db
from application.models import Bands, Venues

db.drop_all()
db.create_all()

# Add some venues to the database

Duchess = Venues(venue_name='The Duchess', venue_loc ='York', start_time ='9pm', entry_fee='£5')

db.session.add(Duchess)
db.session.commit()
