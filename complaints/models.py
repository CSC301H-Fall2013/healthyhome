from django.db import models

class Complaint(models.Model):
	CATEGORIES = (
		('Bed Bugs', 'Bed Bugs'),
		('Cockroaches', 'Cockroaches'),
		('Mice', 'Mice'),
		('Heating', 'Heating'),
		('Plumbing', 'Plumbing'),
		('Elevator Not Working', 'Elevator Not Working'),
		('Repair Order Not Followed', 'Repair Order Not Followed'),
		('Mould', 'Mould'),	
		('Other', 'Other'),
	)
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=250)
	province = models.CharField(max_length=250)
	category = models.CharField(max_length=25, choices=CATEGORIES)
	
#class ContactInfo(models.Model):
	name =  models.CharField(max_length=250)
	number =  models.CharField(max_length=250)
	email =  models.CharField(max_length=250)
