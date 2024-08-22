from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer, ImageUpdate

#Browsing through properties
class PropertyViewSet(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
#Individual property with custom serializer
class PropertyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = ImageUpdate
    lookup_field = "pk"


