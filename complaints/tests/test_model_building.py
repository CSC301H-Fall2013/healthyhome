from django.test import TestCase
from complaints.models import Building


class BuildingTestCase(TestCase):
    """ Tests for the Building model.
    """
    def setUp(self):
        self.b1_name = 'The University of Toronto'
        self.b1_civic_address = '27 King\'s College Circle'
        self.b1_city = 'Toronto'
        self.b1_province = 'Ontario'
        self.b1_latitude = 43.6611024
        self.b1_longitude = -79.39592909999999

        self.b2_name = '#32 27 King\'s College Circle'
        Building.objects.create(
            name=self.b1_name,
            civic_address=self.b1_civic_address,
            city=self.b1_city,
            province=self.b1_province,
            latitude=self.b1_latitude,
            longitude=self.b1_longitude
        )

        Building.objects.create(
            name=self.b2_name,
            civic_address=self.b1_civic_address,
            city=self.b1_city,
            province=self.b1_province,
            latitude=self.b1_latitude,
            longitude=self.b1_longitude
        )

    def test_existence(self):
        """
        Test if building exists in the database.

        """
        building = Building.objects.get(id=1)

        self.assertTrue(building)
        self.assertEqual(self.b1_name, building.name)
        self.assertEqual(self.b1_civic_address, building.civic_address)
        self.assertEqual(self.b1_city, building.city)
        self.assertEqual(self.b1_province, building.province)
        self.assertEqual(self.b1_latitude, building.latitude)
        self.assertEqual(self.b1_longitude, building.longitude)

    def test_valid_slug_simple(self):
        """
        Test if slug fits pattern.

        """
        building = Building.objects.get(id=1)
        expected = 'the-university-of-toronto'

        self.assertEqual(expected, building.slug)

    def test_valid_slug_complex(self):
        """
        Test if slug of name with symbols fits pattern.

        """
        building = Building.objects.get(id=2)
        expected = '32-27-kings-college-circle'

        self.assertEqual(expected, building.slug)

    def test_absolute_url_simple(self):
        """
        Test if URL of building fits pattern.

        """
        building = Building.objects.get(id=1)
        expected = '/building/1/the-university-of-toronto/'

        self.assertEqual(expected, building.get_absolute_url())

    def test_absolute_url_complex(self):
        """
        Test if URL of building that is not first and has more complicated name
        fits pattern.

        """
        building = Building.objects.get(id=2)
        expected = '/building/2/32-27-kings-college-circle/'

        self.assertEqual(expected, building.get_absolute_url())
