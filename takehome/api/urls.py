from django.urls import path
from . import views

urlpatterns = [
    path("properties/", views.PropertyListCreate.as_view(), name = "property-view-create"),
    path("properties/<int:pk>", views.PropertyUpdate.as_view(), name = "update")
]