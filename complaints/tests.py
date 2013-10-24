import unittest
from django.test import Client, TestCase
from complaints.models import Complaint

# Contains all tests for the Complaints class
class ComplaintTestCase(TestCase):
    def setUp(self):

        # Create Complaint fixtures for testing the database
        Complaint.objects.create(lat_long=[37.42426708029149, -122.0840722197085], type="Heating")
        Complaint.objects.create(lat_long=[43.646844, -79.376932], type="Mice")


    def test_valid_complaints(self):

        # Assign variables to fixtures created in database earlier
        heat_problem = Complaint.objects.get(type="Heating")
        mice_problem = Complaint.objects.get(type="Mice")

        # Test to see that variables point to correct fixtures
        self.assertEqual(heat_problem.lat_long, [37.42426708029149, -122.0840722197085])
        self.assertEqual(mice_problem.lat_long, [43.646844, -79.376932])

    def test_irregular_complaints(self):

        # Test when lat_long list is of invalid length
        try:
            Complaint.objects.create(lat_long=[5, 6, 7], type="Elevator Not Working")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

        # Test when type is not any of the possible options that can be chosen
        try:
            Complaint.objects.create(lat_long=[43.646844, -79.376932], type="Unknown")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

# Contains all tests for the Buildings class
class BuildingTestCase(TestCase):
    def setUp(self):

        # Create Building and Complaint fixtures for testing the database
        elevator_complaint = Complaint.objects.create(lat_long=[43.656730, -79.395077], type="Elevator Not Working")
        bedbug_complaint = Complaint.objects.create(lat_long=[43.656730, -79.395077], type="Bed Bugs")
        Building.objects.create(lat_long=[43.656730, -79.395077], complaints=[elevator_complaint, bedbug_complaint])

    def test_valid_buildings(self):

        # Assign variable to fixture created in database earlier
        building = Building.objects.get(lat_long=[43.656730, -79.395077])

        # Test to see that variable points to the correct fixture
        self.assertTrue(building)
        self.assertEqual(building.complaints[0].type, "Elevator Not Working")
        self.assertEqual(building.complaints[1].type, "Bed Bugs")

    def test_invalid_buildings(self):
        # Test when lat_long list is of invalid length
        try:
            Building.objects.create(lat_long=[10], complaints=[])    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

# Contains all tests for the Submission class
class SubmissionTestCase(TestCase):
    def setUp(self):

        # Create Submission fixtures for testing the database
        Submission.objects.create(lat_long=[43.667459, -79.399770], type="Mould")
        Submission.objects.create(lat_long=[43.667991, -79.389895], type="Plumbing")


    def test_valid_submissions(self):

        # Assign variables to fixtures created in database earlier
        mould_problem = Submission.objects.get(type="Mould")
        plumb_problem = Submission.objects.get(type="Plumbing")

        # Test to see that variables point to correct fixtures
        self.assertEqual(mould_problem.lat_long, [43.667459, -79.399770])
        self.assertEqual(mould_problem.lat_long, [43.667991, -79.389895])

    def test_invalid_submissions(self):

        # Test when lat_long list is of invalid length
        try:
            Submission.objects.create(lat_long=[20, 15, 17, 35], type="Other")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

        # Test when type is not any of the possible options that can be chosen
        try:
            Submission.objects.create(lat_long=[43.646844, -79.376932], type="Unknown")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

# Contains all tests for the User class
class UserTestCase(TestCase):
    def setUp(self):

        # Create User fixtures for testing the database
        User.objects.create(name="Fredrick", phone_num="(647)-385-7365", email="fredrick@gmail.com")
        User.objects.create(name="Jane", phone_num="(647)-386-8264", email="jt1985@gmail.com")


    def test_valid_users(self):

        # Assign variables to fixtures created in database earlier
        fredrick = User.objects.get(name="Fredrick")
        jane = User.objects.get(name="Jane")

        # Test to see that variables point to correct fixtures
        self.assertEqual(fredrick.email, "fredrick@gmail.com")
        self.assertEqual(jane.phone_num, "(647)-386-8264")

    def test_invalid_users(self):

        s = 'test' * 15
        # Test when name is length > 50
        try:
            User.objects.create(name=s, phone_num="(647)-387-7589", email="test@gmail.com")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

        # Test whether phone_num only contains numbers
        try:
            User.objects.create(name="Jack", phone_num="(6j7)-bbb-aaaa", email="jker@gmail.com")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception

        # Test whether email is of correct format
        try:
            User.objects.create(name="Kevin", phone_num="(647)-385-6894", email="kvin.com")    # Invalid data
            self.assertTrue(False)  # Code should never reach this point
        except:
            self.assertTrue(True)   # Test if code throws exception


# Contains all the tests regarding POST requests to our web application
class ClientTestCase(TestCase):
    def test_links(self):
        # Act as a client and check if response statuses are normal
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/report/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/report/verify/')
        self.assertEqual(response.status_code, 200)

    def test_valid_complaint_POST(self):
        # Act as a client and send valid data via POST
        response = self.client.post('/report/',
                                    {'lat_long': '[37.42426708029149, -122.0840722197085]', 'type': 'Cockroaches'})
        self.assertEqual(response.status_code, 302) # Check if response is valid

        response = self.client.post('/report/verify/',
                                    {'address': '[43.646844, -79.376932]', 'type': 'Mice'})
        self.assertEqual(response.status_code, 302)

    def test_invalid_complaint_POST(self):
        # Act as a client and send invalid data via POST
        response = self.client.post('/report/', {'address': '[43.646844, -79.376932]', 'type': 'Unknown'})
        self.assertNotEqual(response.status_code, 200) # Check the response is invalid
        response = self.client.post('/report/verify/', {'address': '[43.646844, -79.376932, 53]', 'type': 'Mice'})
        self.assertNotEqual(response.status_code, 200) # Check the response is invalid

    def test_api_call(self):
        # Act as a client and send GET to api
        Building.objects.create(lat_long=[43.656730, -79.395077], complaints=[])
        Building.objects.create(lat_long=[45.756730, -79.395077], complaints=[])
        Building.objects.create(lat_long=[53.658730, -89.395077], complaints=[])
        response = self.client.get('/api/v1/buildings.json')

        # Check if the JSON contains the correct data
        self.assertEqual(response[0][0], 43.656730)
        self.assertEqual(response[1][1], -79.395077)
        self.assertEqual(response[2][0], 53.658730)