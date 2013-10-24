from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from complaints.models import Complaint
from complaints.forms import AddComplaint


class index(ListView):
    model = Complaint


class new(CreateView):
    model = Complaint
    form_class = AddComplaint


class update(UpdateView):
    model = Complaint


class delete(DeleteView):
    model = Complaint