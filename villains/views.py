from django.shortcuts import render
from rest_framework import generics
from .models import Villain 
from .serializer import villainSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class villainsList(generics.ListCreateAPIView):
    queryset = Villain.objects.all()
    serializer_class = villainSerializer
    permission_classes = [IsAuthenticated]


class VillainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Villain.objects.all()
    serializer_class = villainSerializer
    permission_classes = [IsOwnerOrReadOnly]

