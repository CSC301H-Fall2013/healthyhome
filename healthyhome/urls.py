from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from complaints import views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Complaints
                       url(r'^report/', include('complaints.urls')),

                       # Buildings
                       url(r'^building/[0-9]$', views.index.as_view(), name="building"),

                       #Index
                       url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),

                       # Admin
                       url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
                       url(r'^admin/$', include(admin.site.urls)),
)
