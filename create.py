from application import db
from application.models import Bands, Venues

db.drop_all()
db.create_all()

# Add some venues to the database

Duchess = Venues(venue_name='The Duchess', venue_loc ='York', start_time ='9pm', entry_fee='£5')

Brudenell = Venues(venue_name='Brudenell Social Club', venue_loc ='Leeds', 
        start_time ='7:30pm', entry_fee='£12')

Millennium = Venues(venue_name='Millennium Dome', venue_loc ='London',
        start_time ='8:30pm', entry_fee='£60')

db.session.add(Duchess)
db.session.add(Brudenell)
db.session.add(Millennium)
db.session.commit()
