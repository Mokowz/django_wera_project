from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Jobs

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class JobListView(ListView):
    model = Jobs
    template_name = "job_list.html"
    context_object_name = "jobs"

class JobDetailView(DetailView):
    model = Jobs
    template_name = "job_detail.html"
    context_object_name = "job"

class JobCreateView(CreateView):
    model = Jobs
    template_name = "job_create.html"
    fields = ["title", 'payment', "content", ]

    def form_valid(self, form):
        form.instance.employer = self.request.user
        return super().form_valid(form)