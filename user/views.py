from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User_data
from .serializers import UserSerializer
from .permissions import AdminAuthenticationPermission

class UserList(generics.ListCreateAPIView):
    data = User_data.objects.all()
    serializer_data = UserSerializer
    permission_request = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView): 
    data = User_data.objects.all()
    serializer_data = UserSerializer
    permission_request = [AdminAuthenticationPermission]
