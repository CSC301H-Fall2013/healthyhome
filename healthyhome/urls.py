from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from complaints import views

#from complaints.api import BuildingResource, ComplaintResource
#from tastypie.api import Api

admin.autodiscover()

# RESTful API
#v1_api = Api(api_name="v1")
#v1_api.register(ComplaintResource())
#v1_api.register(BuildingResource())

urlpatterns = patterns('',
   # Complaints
   url(r'^report/', include('complaints.urls')),

   # Buildings - this is currently redirecting to same page, will change in next sprint
   url(r'^building/(\d+)$', views.BuildingView.as_view(), name="building"),

   #Index
   url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),

   # API
   # url(r'^api/', include(v1_api.urls)),

   # Admin
   url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
   url(r'^admin/', include(admin.site.urls)),
)
