import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from application import app, db
from flask_bcrypt import Bcrypt
from application.models import Bands, Venues

#Set variables for test band

test_band_name = "The Integrators"
test_genre = "Integral Testing"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('DATABASE_URI'))
        app.config['SECRET_KEY'] = getenv('SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test bands"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='/home/idlorganiser/chromedriver', chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestBand1(TestBase):
    def test_band1(self):
        # Click add band link
        self.driver.find_element_by_xpath("<xpath for Register button in nav bar>").click()
        time.sleep(1)

        # Fill in form
        self.driver.find_element_by_xpath('//*[@id="band_name"]').send_keys(test_band_name)
        self.driver.find_element_by_xpath('//*[@id="genre"]').send_keys(
            test_genre)
        time.sleep(1)

        # Assert that browser redirects to index page
        assert url_for('index') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)

