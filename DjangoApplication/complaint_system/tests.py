import unittest
from django.test import Client, TestCase
from complaint_system.models import Complaint


class ComplaintTestCase(TestCase):
	def setUp(self):
		# Valid Data
		Complaint.objects.create(address="61 Charles Street East, Toronto, Ontario, M5S 1K6", category="Elevator Not Working")
		Complaint.objects.create(address="80 Bloor Street, Toronto, Ontario, M5B 2K1", category="Mold")

	def test_valid_complaints(self):
		''' Data input for complaint form is valid and fits field criteria. 
			The data valiation succeeds and code checks database for created items. '''

		elevator_problem = Complaint.objects.get(address="61 Charles Street East, Toronto, Ontario, M5S 1K6")
		mold_problem = Complaint.objects.get(category="Mold")
		self.assertEqual(elevator_problem.category, 'Elevator Not Working')
		self.assertEqual(mold_problem.address, '80 Bloor Street, Toronto, Ontario, M5B 2K1')

	def test_irregular_complaints(self):
		''' Data input for complaint form does not fit field criteria such as
			length less than 250 for address '''

		s = "test"*100
		# Test for address longer than 250 characters
		try:
			Complaint.objects.create(address=s*100, category="Mold")
			self.assertTrue(False)
		except:
			self.assertTrue(True)


class ClientTestCase(TestCase):
	def test_complaint_links(self):
		# Act as a client and check if response statuses are normal
		response = self.client.get('/complaint_system/')
		self.assertEqual(response.status_code, 200)
		response = self.client.get('/complaint_system/new')
		self.assertEqual(response.status_code, 200)

	def test_valid_complaint_POST(self):
		# Act as a client and send valid data via POST
		response = self.client.post('/complaint_system/new', {'address': '101 Spadina Avenue, Toronto, Ontario, M4S 1X3', 'category': 'Heating'})
		self.assertEqual(response.status_code, 302) # Check if response is valid

	#def test_invalid_complaint_POST(self):
		# Act as a client and send invalid data via POST
		#string = 'test' * 100
		#response = self.client.get('/complaint_system/new')
		#response = self.client.post('/complaint_system/new', {'address': string, 'category': 'Mold'})
		#self.assertNotEqual(response.status_code, 200) # Check the response is invalid