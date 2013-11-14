from django import forms

from form_utils.forms import BetterForm


# This specifies the fields that are in the complaint form
import complaints.views


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

    def __init__(self, *args, **kwargs):
        self.location_data = None
        super(ComplaintForm, self).__init__(*args, **kwargs)

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
            self.location_data = complaints.views.lookup_location(address, city, province)

            if not (cleaned_data.get('bed_bugs') or cleaned_data.get('cockroaches') or
                    cleaned_data.get('mice') or cleaned_data.get('heating') or
                    cleaned_data.get('plumbing') or cleaned_data.get('elevator') or
                    cleaned_data.get('repair_order') or cleaned_data.get('mold') or
                    cleaned_data.get('other')):
                raise forms.ValidationError('At least one complaint needs to be selected.')

            if not self.location_data:
                raise forms.ValidationError('Address was not valid.')

        return cleaned_data

