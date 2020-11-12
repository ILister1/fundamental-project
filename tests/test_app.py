# Import the necessary modules
import unittest
from flask import url_for
from flask_testing import TestCase
from os import getenv

# import the app's classes and objects
from app import app
from application import db
from application.models import Bands

# create the base class for the test app
class TestBase(TestCase):
    def create_app(self):

        # testing config for the app
        app.config.update(SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI'),
                SECRET_KEY = getenv('SECRET_KEY'),
                DEBUG=True
                )
        return app

    def setUp(self):
        # create table
        db.create_all()

        # create test band
        test_band = Bands(band_name='The Testers',genre='Test Genre')
        
        # save band to db
        db.session.add(test_band)
        db.session.commit()

    def tearDown(self):

        #remove the commit, drop the tables
        db.session.remove()
        db.drop_all()

    # Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_home_get(self):

        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code,405)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,405)
