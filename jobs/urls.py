from django.urls import path

from .views import(
    HomePageView,
    JobListView, 
    JobDetailView,
    JobCreateView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("jobs/", JobListView.as_view(), name="job_list"),
    path("jobs/<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("jobs/new/", JobCreateView.as_view(), name="job_new"),
]