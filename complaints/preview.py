from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from complaints.models import Building, Complaint
import complaints.views


class ReportPreview(FormPreview):
    preview_template = 'complaints/preview.html'
    form_template = 'complaints/submit.html'

    def process_preview(self, request, form, context):
        """
        Given a validated form, performs any extra processing before displaying
        the preview page, and saves any extra data in context.
        """
        context['latitude'] = form.location_data['results'][0]['geometry']['location']['lat']
        context['longitude'] = form.location_data['results'][0]['geometry']['location']['lng']

    def done(self, request, cleaned_data):
        """
        Does something with the cleaned_data and returns an
        HttpResponseRedirect.
        """
        address = cleaned_data.get('address')
        city = cleaned_data.get('city')
        province = cleaned_data.get('province')

        del cleaned_data['address']
        del cleaned_data['city']
        del cleaned_data['province']

        location_data = complaints.views.lookup_location(address, city, province)
        latitude = location_data['results'][0]['geometry']['location']['lat']
        longitude = location_data['results'][0]['geometry']['location']['lat']

        if Building.objects.filter(latitude=latitude, longitude=longitude).exists():
            # If the building exists in the database.
            building = Building.objects.get(latitude=latitude, longitude=longitude)
        else:
            # Create a building.
            civic_address = location_data['results'][0]['address_components'][0]['long_name']
            civic_address += ' '
            civic_address += location_data['results'][0]['address_components'][1]['long_name']

            city = location_data['results'][0]['address_components'][4]['long_name']
            province = location_data['results'][0]['address_components'][6]['long_name']

            building = Building(name=civic_address, civic_address=civic_address, city=city, province=province,
                                latitude=latitude, longitude=longitude)
            building.save()

        conversion = {'bed_bugs': 'BB', 'cockroaches': 'CR', 'mice': 'MI', 'heating': 'HE', 'plumbing': 'PB',
                      'elevator': 'EV', 'repair_order': 'RO', 'mold': 'MO', 'other': 'OT'}

        for category, value in cleaned_data.items():
            if value:
                complaint = Complaint(category=conversion[category], building_id=building.id)
                complaint.save()

        return HttpResponseRedirect('/building/1')
