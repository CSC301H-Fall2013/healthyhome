from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect


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
        print cleaned_data
        return HttpResponseRedirect('/building/1')
