from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Creates admin support 
    url(r'^admin/', include(admin.site.urls)), 
    # Regular expression to redirect to complaint system URL and fetch the
	# URLS in the app complaint
    url(r'^complaint_system/', include('complaint_system.urls')),
)
