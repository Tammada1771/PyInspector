
from django.db import models

# Create your models here.
class Location(models.Model):
    Id = models.UUIDField()
    Description = models.CharField(max_length=8)
    
class WorkGroup(models.Model):
    Id = models.UUIDField()
    Description = models.CharField(max_length=100)
    LocationId = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        related_name='WorkGroup'
    )
    
class JobTitle(models.Model):
    Id = models.UUIDField()
    Description = models.CharField(max_length=50)
    WorkGroupId = models.OneToOneField(
       WorkGroup,
       on_delete=models.CASCADE,
       related_name='JobTitle'
    )
    
    def __str__(self):
        return self.Description
    
