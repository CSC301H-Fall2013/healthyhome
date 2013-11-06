from django.test import TestCase
from complaints.models import Complaint

class VerificationTestCase(TestCase):
	def setUp(self):

		#create a Submissions and verification
		Submission.objects.create(lag_long=[43.667459, -79.399770], type="Mould")
		Submission.objects.create(lag_long=[43.667459, -79.399770], type="Plumbing")
		V1 = Verification(43.667459, -79.399770, [Mould_complaint, Plumbing_complaint])



	def test_correct_verification(self):

		self.assertEqual(mould_problem.lat_long[0],V1.lat)
		self.assertEqual(mould_problem.lat_long[1],V1.long)

		self.assertEqual(plumb_problem.lat_long[0],V1.lat)
		self.assertEqual((plumb_problem.lat_long[1],V1.long)

		self.assertEqualmould_problem.type,V1.type[0])
		self.assertEqual(plumb_problem.type,V1.type[1])
	# how should I test verification time


	def test_incorrect_verification(self):

		# test invalid alt_long
		try:
			V = Verification(43, 76, 10, 100, 89, Mould_complaint, Plumbing_complaint)
			self.assertTrue(false)
		except:
			self.assertTrue(True)

	    # test invalid type
		try:
			Verification(100, 200, "abc")
		    self.assertTrue(false)
		except:
			self.assertTrue(True)






