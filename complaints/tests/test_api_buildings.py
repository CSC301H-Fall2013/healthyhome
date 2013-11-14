from django.test import TestCase
from complaints.models import Complaint, Building
import json
import urllib2


class ApiTestCase(TestCase):
    """ Tests the API for Buildings.
    """
    def setUp(self):
        self.b1_name = 'The University of Toronto'
        self.b1_civic_address = '27 King\'s College Circle'
        self.b1_city = 'Toronto'
        self.b1_province = 'Ontario'
        self.b1_latitude = 43.6611024
        self.b1_longitude = -79.39592909999999

        Building.objects.create(
            name=self.b1_name,
            civic_address=self.b1_civic_address,
            city=self.b1_city,
            province=self.b1_province,
            latitude=self.b1_latitude,
            longitude=self.b1_longitude
        )

        Complaint.objects.create(
            building_id=1,
            category='BB',
        )

        Complaint.objects.create(
            building_id=1,
            category='HE',
        )

        Complaint.objects.create(
            building_id=1,
            category='MO',
        )

    def test_valid_API_data(self):
        """
        Test if API returns correct information from database.

        """
        response = urllib2.urlopen('http://localhost:8000/api/v1/buildings/')
        result = json.loads(response.read())
        self.assertEqual(result[0]['lat'], 43.6611024)
        self.assertEqual(result[0]['lng'], -79.39592909999999)
        self.assertEqual(result[0]['title'], 'The University of Toronto')
        self.assertEqual(result[0]['id'], 1)
