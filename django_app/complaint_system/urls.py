from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from complaint_system import views

urlpatterns = patterns('',
	url(r'^$', views.index.as_view(), name='index'),
	url(r'^new', views.new.as_view(success_url="/complaint_system/success/"), name='new'),
	#url(r'^edit/(?P<pk>\d+)$', views.update.as_view(), name='edit'),
	#url(r'^delete/(?P<pk>\d+)$', views.delete.as_view(success_url="/complaint_system/"), name='delete'),
	url(r'^success/', TemplateView.as_view(template_name='complaint_system/complaint_success.html'), name="success"),
)