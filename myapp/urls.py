from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("contact-list/", views.contact_list, name="contact_list"),
    path("name/<str:name>/", views.name, name="name"),
    # Dynamic Template Demo URLs
    path(
        "template-features/",
        views.template_features_demo,
        name="template_features_demo",
    ),
    path("custom-tags-demo/", views.custom_template_tags_demo, name="custom_tags_demo"),
]
