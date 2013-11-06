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

    lat = models.FloatField()
    long = models.FloatField()
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type


class Building(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    lat = models.FloatField()
    long = models.FloatField()
    type = models.CharField(max_length=25, choices=Complaint.CATEGORIES)

    def __unicode__(self):
        return (self.lat, self.long)


class Submission(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    lat = models.FloatField()
    long = models.FloatField()
    type = models.CharField(max_length=25, choices=Complaint.CATEGORIES)
    time_created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return (self.lat, self.long)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    def __unicode__(self):
        return self.name

class Verification(models.Model):
	def __init__(self, lat, long, type)
	self.lat = models.FloatField()
	self.long = models.FloatField()
	self.type = models.CharField(max_length=25, choices=Complaint.CATEGORIES)
	self.time_created = models.DateField(auto_now_add=True)

def __unicode__(self):
	return (self.time_created)

