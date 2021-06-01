from django.db.models import fields
from rest_framework import serializers
from .models import Location, Region, Size, WorkGroup, JobTitle, User, Region, Size


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')


class WorkGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkGroup
        fields = ('id', 'name', 'location')


class JobTitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobTitle
        fields = ('id', 'name', 'workgroup')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'employeeId', 'password', 'employeeType', 'email', 'cellphone', 'workphone', 'location', 'jobtitle', 'supervisorId')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')
        

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')