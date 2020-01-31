from apps.accounts.serializers import ProfileSerializer
from apps.accounts.models import Profile

from rest_framework import generics
from django.shortcuts import render

class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer