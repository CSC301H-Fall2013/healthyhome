from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   # Complaints
   url(r'^report/', include('complaints.urls')),

   # Buildings - this is currently redirecting to same page, will change in next sprint
   url(r'^building/(\d+)$','complaints.views.building'),

   #Index
   url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),

   # API
   url(r'^api/v1/buildings/$', 'complaints.views.buildings_api'),

   # Admin
   url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
   url(r'^admin/', include(admin.site.urls)),
)
