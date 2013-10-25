from django.views.generic import ListView
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from complaints.models import Complaint
from complaints.forms import AddComplaint
import urllib2	# Library to open URLs in Python
import json # Library for encoding and decoding jsons

class index(ListView):
    model = Complaint

def report(request):
    # sticks in a POST or renders empty form
    form = AddComplaint(request.POST or None)
    if form.is_valid():
    	form_query = form.cleaned_data
        #complaint = form.save()

        # Query the Google Maps API and return the result JSON
        map_address = '+'.join(str(form_query['address']).split())
        map_city = '+'.join(str(form_query['city']).split())
        map_prov = '+'.join(str(form_query['province']).split())
        result = urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?address='+map_address+',+' + map_city +',+' + map_prov + '&sensor=true')
        content = result.read()
        content_json = json.loads(content) # Creates a json object that we can query easily
        # Check if the result is an invalid address
        if content_json["status"] == "ZERO_RESULTS":
        	return render_to_response('complaints/complaint_form.html', {'form': form}, context_instance=RequestContext(request))
        else:
        	complaint = form.save(commit=False)
        	complaint.lat = content_json["results"][0]["geometry"]["location"]["lat"]
        	complaint.long = content_json["results"][0]["geometry"]["location"]["lng"]
        	complaint.save()
        	return redirect('/building/1')
        	#return render_to_response('fake.html', {'form_query': form_query}, context_instance=RequestContext(request))
        #complaint.save()
        #return redirect(complaints)
    return render_to_response('complaints/complaint_form.html', {'form': form}, context_instance=RequestContext(request))