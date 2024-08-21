from django.shortcuts import render
from rest_framework import generics
from .models import Property
from .serializers import PropertySerializer

class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

