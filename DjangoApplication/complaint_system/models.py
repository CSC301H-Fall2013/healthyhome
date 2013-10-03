from django.db import models

class Complaint(models.Model):
	CATEGORIES = (
		('Bed Bugs', 'Bed Bugs'),
		('Cockroaches', 'Cockroaches'),
		('Mice', 'Mice'),
		('Heating', 'Heating'),
		('Plumbling', 'Plumbling'),
		('Elevator Not Working', 'Elevator Not Working'),
		('Repair Order Not Followed', 'Repair Order Not Followed'),
		('Mold', 'Mold'),	
		('Other', 'Other'),
	)
	address = models.CharField(max_length=250)
	category = models.CharField(max_length=25, choices=CATEGORIES)