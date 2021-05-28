
from django.db import models


# Create your models here.
class Location(models.Model):
    Id = models.UUIDField()
    Description = models.CharField(max_length=8)
    
class WorkGroup(models.Model):
    Id = models.UUIDField()
    Description = models.CharField(max_length=100)
    LocationId = models.ForeignKey(
        Location.Id,
        verbose_name=("WorkGroup"),
        on_delete=models.CASCADE
        )   
    
class JobTitle(models.Model):
    Id = models.UUIDField()
    Description = models.CharField(max_length=50)
    WorkGroupId = models.ForeignKey(
        WorkGroup.Id,
        verbose_name=('JobTitle'),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.Description
    
