from rest_framework import serializers
from .models import Location
from .models import WorkGroup
from .models import JobTitle


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
