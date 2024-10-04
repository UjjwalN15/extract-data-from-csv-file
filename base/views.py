from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
# Create your views here.

class CollegeApiViewsets(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer