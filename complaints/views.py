from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from complaints.models import Complaint


class index(ListView):
    model = Complaint


class new(CreateView):
    model = Complaint


class update(UpdateView):
    model = Complaint


class delete(DeleteView):
    model = Complaint