from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect
from complaints.models import Building
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

        if False:
            # If the building exists
            building = None
        else:
            pass
            # Create a building.
            #civic_address =
            #city =
            #province =
            #building = Building(name=civic_address, civic_address=civic_address, city=city, province=province,
            #                    latitude=latitude, longitude=longitude)
            #building.save()
        for c_type, value in cleaned_data.items:
            if value:
                c_type.upper()
        print cleaned_data
        return HttpResponseRedirect('/building/1')
