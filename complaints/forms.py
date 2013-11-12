from django import forms

from complaints.models import Complaint


# This specifies the fields that are in the complaint form
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['category']

    address = forms.CharField(label='Address', max_length=250, required=True)
    city = forms.CharField(label='City', max_length=250, required=True)
    province = forms.CharField(label='Province', max_length=250, required=True)

    category = forms.MultipleChoiceField(choices=Complaint.CATEGORY_CHOICES, widget=forms.CheckboxSelectMultiple(), required=True)
