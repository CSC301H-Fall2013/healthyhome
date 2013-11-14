from tastypie.resources import ModelResource
from complaints.models import Building, Complaint
from tastypie import fields


class BuildingResource(ModelResource):
    complaints = fields.ToManyField('complaints.api.ComplaintResource', 'complaints', full=True)

    class Meta:
        queryset = Building.objects.all()
        resource_name = 'entry'


class ComplaintResource(ModelResource):
    class Meta:
        queryset = Complaint.objects.all()
        resource_name = 'entry'
