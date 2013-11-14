import urllib2
import json
from django import forms

from form_utils.forms import BetterForm


# This specifies the fields that are in the complaint form
class ComplaintForm(BetterForm):
    # Group fields into fieldsets.
    class Meta:
        fieldsets = [('address', {'fields': ['address', 'city', 'province']}),
                     ('complaints', {'fields': ['bed_bugs', 'cockroaches', 'mice', 'heating', 'plumbing',
                                                'elevator', 'repair_order', 'mold', 'other']})]

    # Address for the complaints.
    address = forms.CharField(label='Address', max_length=250, required=True)
    city = forms.CharField(label='City', max_length=250, required=True)
    province = forms.CharField(label='Province', max_length=250, required=True)

    # Types of complaints.
    bed_bugs = forms.BooleanField(required=False)
    cockroaches = forms.BooleanField(required=False)
    mice = forms.BooleanField(required=False)
    heating = forms.BooleanField(required=False)
    plumbing = forms.BooleanField(required=False)
    elevator = forms.BooleanField(required=False)
    repair_order = forms.BooleanField(required=False)
    mold = forms.BooleanField(required=False)
    other = forms.BooleanField(required=False)

    def clean(self):
        """
        Hook for doing any extra form-wide cleaning after Field.clean() been
        called on every field. Any ValidationError raised by this method will
        not be associated with a particular field; it will have a special-case
        association with the field named '__all__'.
        """
        cleaned_data = super(ComplaintForm, self).clean()

        address = cleaned_data.get('address')
        city = cleaned_data.get('city')
        province = cleaned_data.get('province')

        if address and city and province:
            location = lookup_location(address, city, province)
            print location

            if location:
                latitude = location["results"][0]["geometry"]["location"]["lat"]
                longitude = location["results"][0]["geometry"]["location"]["lng"]
            else:
                raise forms.ValidationError("Address was not valid.")

        return cleaned_data


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

