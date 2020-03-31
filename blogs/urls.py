from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<int:blog_id>/", views.detail, name="detail"),
]
