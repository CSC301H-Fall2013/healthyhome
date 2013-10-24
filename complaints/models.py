from django.db import models

# This is the Complaint model, other models will be implemented here in Sprint 2.
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
