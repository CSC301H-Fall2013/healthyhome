import urllib2  # Open URLs in python
import json     # Encode and Decode JSON

from django.shortcuts import render

from complaints.models import Building, Complaint
from django.http import HttpResponse


def buildings_api(request):
    all_buildings = Building.objects.all()
    data = []
    for b in all_buildings:
        new_obj = {}
        new_obj['lat'] = b.latitude
        new_obj['lng'] = b.longitude
        new_obj['title'] = b.name
        new_obj['id'] = b.id
        new_obj['categories'] = []
        for complaint in b.complaint_set.all():
            current_category = Complaint.CATEGORY_NAMES[complaint.category]
            new_obj['categories'].append(current_category)

        data.append(new_obj)

    return HttpResponse(json.dumps(data), content_type='application/json')


def building(request, bid):
    # sticks in a POST or renders empty form
    selected_building = Building.objects.get(id=bid)
    complaints = Complaint.objects.filter(building_id=bid)
    categories = {}
    for complaint in complaints:
        name = Complaint.CATEGORY_NAMES[complaint.category]
        if name in categories:
            categories[name] += 1
        else:
            categories[name] = 1

    return render(request, 'complaints/building_page.html', {'categories': categories, 'building': selected_building})


def lookup_location(address, city, province):
    """
    Return the location of the address specified in data as a JSON object. If the address
    is invalid, return the empty string.
    @return:
    """
    print address, city, province
    address = '+'.join(address.split())
    city = '+'.join(city.split())
    province = '+'.join(province.split())

    result = urllib2.urlopen(
        'http://maps.googleapis.com/maps/api/geocode/json?address=' +
        address + ',+' + city + ',+' + province + '&sensor=true')
    result = json.loads(result.read())

    if result['status'] == 'ZERO_RESULTS':
        result = ''
    return result
