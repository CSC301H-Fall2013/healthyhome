from django.views.generic import ListView
from django.views.generic.edit import CreateView

from complaint_system.models import Complaint

class index(ListView):
	model = Complaint

class new(CreateView):
	model = Complaint