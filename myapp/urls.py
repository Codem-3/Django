from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("contact-list/", views.contact_list, name="contact_list"),
    path("name/<str:name>/", views.name, name="name"),
]
