from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserSerialize
# Create your views here.

class CreateUser(generics.ListCreateAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
class UserUpdateDestroy(generics.RetrieveUpdateDestroyAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerialize
    lookup_field="pk"
    
    
