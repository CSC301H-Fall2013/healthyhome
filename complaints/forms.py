from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from complaints.models import Complaint

# This specifies the fields that are in the complaint form
class AddComplaint(forms.ModelForm):
    address = forms.CharField(max_length=250, required = True)
    city = forms.CharField(max_length=250, required = True)
    province = forms.CharField(max_length=250, required = True)
    categories = forms.MultipleChoiceField(choices=Complaint.CATEGORIES, widget=forms.CheckboxSelectMultiple(), required = True)

    class Meta:
        model = Complaint

    name =  forms.CharField(max_length=250)
    number =  forms.CharField(max_length=250)
    email =  forms.CharField(max_length=250)

    #def clean(self):
        #num = filter(lambda e:e,[Complaint.number, Complaint.email])
        #if not bool(number) or bool(email):
            #raise ValidationError("at least one piece of contact information must be set")
