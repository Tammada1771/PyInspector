from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LocationSerializer, WorkGroupSerializer, JobTitleSerializer, UserSerializer, RegionSerializer, SizeSerializer

from .models import Location, WorkGroup, JobTitle, User, Region, Size


# Create your views here.


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('name')
    serializer_class = LocationSerializer


class WorkGroupViewSet(viewsets.ModelViewSet):
    queryset = WorkGroup.objects.all().order_by('name')
    serializer_class = WorkGroupSerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all().order_by('name')
    serializer_class = JobTitleSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('employeeId')
    serializer_class = UserSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('name')
    serializer_class = RegionSerializer
    
    
class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all().order_by('name')
    serializer_class = SizeSerializer
