from django.shortcuts import render
from rest_framework import viewsets

from .serializers import LocationSerializer
from .serializers import WorkGroupSerializer
from .serializers import JobTitleSerializer
from .models import Location
from .models import WorkGroup
from .models import JobTitle

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
