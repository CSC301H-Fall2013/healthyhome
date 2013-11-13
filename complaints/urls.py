from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from complaints.forms import ComplaintForm
from complaints.preview import ReportPreview

urlpatterns = patterns('',
                       url(r'^$', ReportPreview(ComplaintForm))
)
