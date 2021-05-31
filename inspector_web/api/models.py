from ast import Num
import uuid

from django.db import models
from django.db.models.deletion import CASCADE
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
    
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employeeId = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    employeeType = models.IntegerField(max_length=2)
    email = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=10)
    workphone = models.CharField(max_length=10)
    location = models.ForeignKey(
        Location,
        verbose_name=('Location'),
        on_delete=models.CASCADE
    )
    jobtitle = models.ForeignKey(
        JobTitle,
        verbose_name=('JobTitle'),
        on_delete=models.CASCADE
    )
    supervisorId = models.CharField(max_length=10)
    
    def __str__(self):
        return self.employeeId
    
    
class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Size(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
    
class Stations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    region = models.ForeignKey(
        Region,
        verbose_name=('Region'),
        on_delete=models.CASCADE
    )
    numInspections = models.IntegerField()
    company = models.CharField(max_length=50)
    size = models.ForeignKey(
        Size,
        verbose_name=('Size'),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
    

class InspectionType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
        
class Inspection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    station = models.ForeignKey(
        Stations,
        verbose_name=('Station'),
        on_delete=models.CASCADE
    )
    employee = models.CharField(max_length=10)
    inspectionType = models.ForeignKey(
        InspectionType,
        verbose_name=('InspectionType'),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.startdate
    
    
class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name
    
    
class EquipmentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Equipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipmentType = models.ForeignKey(
        EquipmentType,
        verbose_name=('EquipmentType'),
        on_delete=models.CASCADE
    )
    equipmentClass = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serialNumber = models.CharField(max_length=50)
    equipmentNumber = models.CharField(max_length=75)
    station = models.ForeignKey(
        Stations,
        verbose_name=('Station'),
        on_delete=models.CASCADE
    )
    voltage = models.CharField(max_length=7)
    equipmentPosition = models.CharField(max_length=50)
    region = models.ForeignKey(
        Region,
        verbose_name=('Region'),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.equipmentNumber
    
    
class Alert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    alerter = models.ForeignKey(
        User,
        verbose_name=('Alerter'),
        on_delete=models.CASCADE
    )
    alerted = models.ForeignKey(
        User,
        verbose_name=('Alerted'),
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=max)
    status = models.ForeignKey(
        Status,
        verbose_name=('Status'),
        on_delete=models.CASCADE
    )
    equipment = models.ForeignKey(
        Equipment,
        verbose_name=('Equipment'),
        on_delete=models.CASCADE
    )
    station = models.ForeignKey(
        Stations,
        verbose_name=('Station'),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.status


class MxOrderType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
 
class MxOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(
        MxOrderType,
        verbose_name=('Type'),
        on_delete=models.CASCADE
    )
    issuer = models.ForeignKey(
        User,
        verbose_name=('Issuer'),
        on_delete=models.CASCADE
    )
    date = models.DateTimeField()
    station = models.ForeignKey(
        Stations,
        verbose_name=('Station'),
        on_delete=models.CASCADE
    )
    equipment = models.ForeignKey(
        Equipment,
        verbose_name=('Equipment'),
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.type
    
    
class EquipBattery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )


    