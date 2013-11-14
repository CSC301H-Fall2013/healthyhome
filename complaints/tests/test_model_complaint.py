from django.test import TestCase
from complaints.models import Complaint, Building


class ComplaintTestCase(TestCase):
    """ Tests for the Building model.
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

    def test_existence(self):
        """
        Test if complaints exist in the database.

        """
        complaint1 = Complaint.objects.get(id=1)
        complaint2 = Complaint.objects.get(id=2)
        complaint3 = Complaint.objects.get(id=3)

        self.assertTrue(complaint1)
        self.assertTrue(complaint2)
        self.assertTrue(complaint3)

        # Test if variables point to correct fixtures
        self.assertEqual('BB', complaint1.category)
        self.assertEqual('HE', complaint2.category)
        self.assertEqual('MO', complaint3.category)

    def test_invalid_category(self):
        """
        Test if complaint is associated to an invalid category.

        """
        try:
            Complaint.objects.create(building_id=1, category='IN')
            self.assertTrue(False)    # Code should never reach this point
        except:
            self.assertTrue(True)     # Test if code throws exception

    def test_invalid_bid(self):
        """
        Test if complaint is associated to an non-existent building.

        """
        try:
            Complaint.objects.create(building_id=2, category='PB')
            invalid_building_id = True      # Code should never reach this point
        except:
            invalid_building_id = False     # Test if code throws exception

        self.assertTrue(invalid_building_id)