from django.db import models
from django.template.defaultfilters import slugify


class Complaint(models.Model):
    BED_BUGS = 'BB'
    COCKROACHES = 'CR'
    MICE = 'MI'
    HEATNG = 'HE'
    PLUMBING = 'PB'
    ELEVATOR = 'EV'
    REPAIR_ORDER = 'RO'
    MOLD = 'MO'
    OTHER = 'OT'

    CATEGORY_NAMES = {
        BED_BUGS : 'Bed Bugs',
        COCKROACHES : 'Cockroaches',
        MICE : 'Mice',
        HEATNG : 'Heating',
        PLUMBING : 'Plumbing',
        ELEVATOR : 'Elevator Not Working',
        REPAIR_ORDER : 'Repair Order Not Followed',
        MOLD : 'Mold',
        OTHER : 'Other'
    }

    CATEGORY_CHOICES = (
        (BED_BUGS, CATEGORY_NAMES[BED_BUGS]),
        (COCKROACHES, CATEGORY_NAMES[COCKROACHES]),
        (MICE, CATEGORY_NAMES[MICE]),
        (HEATNG, CATEGORY_NAMES[HEATNG]),
        (PLUMBING, CATEGORY_NAMES[PLUMBING]),
        (ELEVATOR, CATEGORY_NAMES[ELEVATOR]),
        (REPAIR_ORDER, CATEGORY_NAMES[REPAIR_ORDER]),
        (MOLD, CATEGORY_NAMES[MOLD]),
        (OTHER, CATEGORY_NAMES[OTHER])
    )

    building = models.ForeignKey('Building')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.timestamp.strftime('%d %b, %Y') + ' ' + str(self.category)


class Building(models.Model):
    # Name for the building
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)

    # Street number, Street name and Unit number is stored in civic_address
    civic_address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)  # Newly created object, so set slug

        super(Building, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/building/{0}/{1}/'.format(self.id, self.slug)

    def __unicode__(self):
        return self.name