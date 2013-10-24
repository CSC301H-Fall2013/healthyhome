from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from complaints import views

urlpatterns = patterns('',
                       url(r'^$', views.new.as_view(success_url="/report/verify/"), name='new'),
                       url(r'^verify/$', TemplateView.as_view(template_name='complaints/complaint_verify.html'), name="verify"),
)