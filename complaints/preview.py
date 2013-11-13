from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect

__author__ = 'Noel'


class ReportPreview(FormPreview):
    preview_template = 'complaints/preview.html'
    form_template = 'complaints/submit.html'

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.
        return HttpResponseRedirect('/building/1')
