from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from complaints import views

urlpatterns = patterns('',
       url(r'^$', 'complaints.views.report'),
       url(r'^verify/$', TemplateView.as_view(template_name='complaints/complaint_verify.html'), name="verify"),
)