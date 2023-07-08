from django.shortcuts import render
from rest_framework import generics
from .models import Villain 
from .serializer import villainSerializer

# Create your views here.
class villainsList(generics.ListCreateAPIView):
    queryset = Villain.objects.all()
    serializer_class = villainSerializer

class VillainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Villain.objects.all()
    serializer_class = villainSerializer

