import uuid

from django.db import models
from django.db.models.fields.related import ForeignKey


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class WorkGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(
        Location,
        verbose_name=("Location"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class JobTitle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    workgroup = models.ForeignKey(
        WorkGroup,
        verbose_name=('WorkGroup'),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
