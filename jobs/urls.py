from django.urls import path

from . import views

app_name = "job"

urlpatterns = [
    path("jobs", views.home, name="home"),
    path("apply/<int:job_id>", views.apply, name="apply"),
    path("save", views.save_apply, name="save"),
]
