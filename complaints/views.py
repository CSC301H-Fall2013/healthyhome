import urllib2  # Open URLs in python
import json     # Encode and Decode JSON

from django.views.generic import ListView
from django.shortcuts import redirect, render

from complaints.models import Complaint
from complaints.forms import ComplaintForm


class index(ListView):
    model = Complaint


def report(request):
    # sticks in a POST or renders empty form
    form = ComplaintForm(request.POST or None)
    if form.is_valid():
        form_query = form.cleaned_data
        #complaint = form.save()

        # Query the Google Maps API and return the result JSON
        map_address = '+'.join(str(form_query['address']).split())
        map_city = '+'.join(str(form_query['city']).split())
        map_prov = '+'.join(str(form_query['province']).split())
        result = urllib2.urlopen(
            'http://maps.googleapis.com/maps/api/geocode/json?address=' + map_address + ',+' + map_city + ',+' + map_prov + '&sensor=true')
        content = result.read()
        content_json = json.loads(content) # Creates a json object that we can query easily
        # Check if the result is an invalid address
        if content_json["status"] == "ZERO_RESULTS":
            return render(request, 'complaint/submit.html', {'form': form})
        else:
            complaint = form.save(commit=False)
            complaint.lat = content_json["results"][0]["geometry"]["location"]["lat"]
            complaint.long = content_json["results"][0]["geometry"]["location"]["lng"]
            complaint.save()
            return redirect('/building/1')
            #complaint.save()
            #return redirect(complaints)
    return render(request, 'complaint/submit.html', {'form': form})
