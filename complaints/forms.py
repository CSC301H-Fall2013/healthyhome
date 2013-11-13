from django import forms

from form_utils.forms import BetterForm


# This specifies the fields that are in the complaint form
class ComplaintForm(BetterForm):
    # Address for the complaints.
    civic = forms.CharField(label='Address', max_length=250, required=True)
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

    class Meta:
        fieldsets = [('address', {'fields': ['civic', 'city', 'province']}),
                     ('complaints', {'fields': ['bed_bugs', 'cockroaches', 'mice', 'heating', 'plumbing',
                                                'elevator', 'repair_order', 'mold', 'other']})]

