from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from complaint_system import views

urlpatterns = patterns('',
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^new', views.new.as_view(success_url="/complaint_system/success/"), name='new'),
	url(r'^success/', TemplateView.as_view(template_name='complaint_system/complaint_success.html'), name="success"),
)