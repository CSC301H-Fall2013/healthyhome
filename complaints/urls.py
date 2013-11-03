from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
                       url(r'^$', 'complaints.views.report'),
                       url(r'^verify/$', TemplateView.as_view(template_name='complaints/complaint_verify.html'),
                           name="verify"),
)
