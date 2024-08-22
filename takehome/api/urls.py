from django.urls import path
from . import views

urlpatterns = [
    #Properties browsing
    path("properties/", views.PropertyViewSet.as_view(), name = "property-view-create"),
    #Individual Properites based on id
    path("properties/<int:pk>", views.PropertyUpdate.as_view(), name = "update")
]