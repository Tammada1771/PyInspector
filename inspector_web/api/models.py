
import uuid

from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# the location of the employee, ie the service center
class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=8)

    def __str__(self):
        return self.name


# the group the job title falls into
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


# the title of an employee
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


#used to store all the information for a user    
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employeeId = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    employeeType = models.IntegerField()
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
    

#used to set the region that a station is in    
class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

#used to store the size of a station   
class Size(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        

#used to store all the stations    
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
    

#used to determine the type of inspection, ie station or battery
class InspectionType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

#used to keep track of a base inspection, all pieces of equipment in the inspection will also have a row        
class Inspection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    duration = models.DateTimeField(null=True)
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
    

#used to set the status of a alert or mxorder, ie unaknowledged aknowledged inprocess   
class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name
    

#types of equipment, ie transformer, battery, charger, vacrecloser   
class EquipmentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

# this is the nameplate for all different types of equipment, all equipment has one    
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
    

# alerts are used to inform of problems at stations during inspections  
class Alert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    alerter = models.CharField(max_length=10)
    alerted = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
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


# used to create a new work order type at a station
class MxOrderType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
 
       
# used to create a new work order at a station
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
    

# Equipment at stations, here down -- inspector fills these fields out -- fields are nullable so that an inspection and be saved as it is filled out -- row inserted per inspection ---->    
class Battery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    cellElectolyteLevel = models.CharField(max_length=50, null=True)
    cellFreeLeaks = models.BooleanField(null=True)
    postStrapFreeCorro = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class BatteryInspection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    tempBatRoom = models.IntegerField(null=True)
    ventChecked = models.BooleanField(null=True)
    rackCond = models.BooleanField(null=True)
    cellElectolyteLevel = models.CharField(max_length=50, null=True)
    cellFreeLeaks = models.BooleanField(null=True)
    deminWaterAdded = models.BooleanField(null=True)
    postStrapFreeCorro = models.BooleanField(null=True)
    positiveGround = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    negativeGround = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    vlaGroundTestRatio = models.DecimalField(null=True, decimal_places=1, max_digits=5)
    floatVolts = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    floatAmps = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    ampUnits = models.CharField(max_length=25, null=True)
    charger1Volt = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    charger1Amp = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    charger2Volt = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    charger2Amp = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    charger3Volt = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    charger3Amp = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    

class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    groundIntact = models.BooleanField(null=True)
    phonelineClear = models.BooleanField(null=True)
    lightsWork = models.BooleanField(null=True)
    operatingInstrct = models.BooleanField(null=True)
    onelineDia = models.BooleanField(null=True)
    spareFuseQntOk = models.BooleanField(null=True)
    stationInfo = models.BooleanField(null=True)
    acdcPanelGoodCond = models.BooleanField(null=True)
    acdcPanelFlagFree = models.BooleanField(null=True)
    relayPanelGoodCond = models.BooleanField(null=True)
    indicateLightsSvcPanel = models.BooleanField(null=True)
    hvacFanOp = models.BooleanField(null=True)
    toolEquipGoodCond = models.BooleanField(null=True)
    fireExtCharged = models.BooleanField(null=True)
    fireExtTagSign = models.BooleanField(null=True)
    exitLightOp = models.BooleanField(null=True)
    thermSetCool75Heat55 = models.BooleanField(null=True)
    siliconWipeStock = models.BooleanField(null=True)
    operatingInstructDate = models.DateTimeField(null=True)
    floorCleanGoodcond = models.BooleanField(null=True)
    freeRodent = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class Charger(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    volt = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    amp = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    noGroundPres = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class VacBreakerIndoor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    heaterCond = models.CharField(max_length=25, null=True)
    counter = models.IntegerField(null=True)
    operatorCharged = models.BooleanField(null=True)
    breakerCubGoodCond = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class OilBreaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    #need to add the rest of the fields
    
    def __str__(self):
        return self.inspection


class VacRecloser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    surgeArrestors = models.CharField(max_length=25, null=True)
    counter = models.IntegerField(null=True)
    bushings = models.CharField(max_length=25, null=True)
    connectionsGoodCond = models.BooleanField(null=True)
    tankGoodCond = models.BooleanField(null=True)
    oilLeaks = models.BooleanField(null=True)
    animalProtectGoodCond = models.BooleanField(null=True)
    potheadGoodCond = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class Yard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    weather = models.CharField(max_length=25, null=True)
    landscapingGoodCond = models.BooleanField(null=True)
    gatesDoorsGoodCond = models.BooleanField(null=True)
    groundsGateIntact = models.BooleanField(null=True)
    perimeterGoodCond = models.BooleanField(null=True)
    noHoleFabric = models.BooleanField(null=True)
    rampartGoodCond = models.BooleanField(null=True)
    groundsIntact40ft = models.BooleanField(null=True)
    gapsLess6in = models.BooleanField(null=True)
    warningSignGate = models.BooleanField(null=True)
    exterLightGoodCond = models.BooleanField(null=True)
    freeVegInside = models.BooleanField(null=True)
    freeLiter = models.BooleanField(null=True)
    freeItemsStored = models.BooleanField(null=True)
    cableTrenchGoodCond = models.BooleanField(null=True)
    lightningMastGoodCond = models.BooleanField(null=True)
    stoneGoodCond = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    climbingAssist4ft = models.BooleanField(null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class SF6Breaker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    counter = models.IntegerField(null=True)
    operatorGoodCond = models.BooleanField(null=True)
    controlCabGoodCond = models.BooleanField(null=True)
    gasPressInLimit = models.BooleanField(null=True)
    gasPress = models.IntegerField(null=True)
    standGoodCond = models.BooleanField(null=True)
    bushings = models.CharField(max_length=50, null=True)
    connectionsGoodCond = models.CharField(max_length=50, null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    potheadGoodCond = models.BooleanField(null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        related_name=('InspectionId'),
        on_delete=models.CASCADE
    )
    conductorGoodCond = models.BooleanField(null=True)
    freeBirdInsect = models.BooleanField(null=True)
    disconnectSwitchGoodCond = models.BooleanField(null=True)
    insulatorGoodCond = models.BooleanField(null=True)
    ptsGoodCond = models.BooleanField(null=True)
    ptFusesGoodCond = models.BooleanField(null=True)
    auxTRFGoodCond = models.BooleanField(null=True)
    auxTRFFusesGoodCond = models.BooleanField(null=True)
    animalProtectGoodCond = models.BooleanField(null=True)
    groundIntact = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    ctGoodCond = models.BooleanField(null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class CapacitorBank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    freeBulgedCans = models.BooleanField(null=True)
    signsPerimeter = models.BooleanField(null=True)
    pdPtCtGoodCond = models.BooleanField(null=True)
    fusesIntact = models.BooleanField(null=True)
    surgeArrestors = models.CharField(max_length=25, null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    

class Transformer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    counter = models.IntegerField(null=True)
    didCountRoll = models.BooleanField(null=True)
    lowerDrag = models.CharField(max_length=3, null=True)
    raiseDrag = models.CharField(max_length=3, null=True)
    oilLevel = models.CharField(max_length=25, null=True)
    currentWindTemp = models.IntegerField(null=True)
    maxWindTemp = models.IntegerField(null=True)
    currentTopTemp = models.IntegerField(null=True)
    maxTopTemp = models.IntegerField(null=True)
    mainTankPress = models.CharField(max_length=25, null=True)
    n2BottlePress = models.IntegerField(null=True)
    n2SysGoodCond = models.BooleanField(null=True)
    ltcOilLevel = models.CharField(max_length=25, null=True)
    dessocantColor = models.CharField(max_length=25, null=True)
    hvBushCond = models.CharField(max_length=25, null=True)
    lvBushCond = models.CharField(max_length=25, null=True)
    surgeArrestorCond = models.CharField(max_length=25, null=True)
    pressReliefNotAct = models.BooleanField(null=True)
    suddenPressValveOpen = models.BooleanField(null=True)
    heatersWorkProp = models.BooleanField(null=True)
    cabClean = models.BooleanField(null=True)
    radiatorGoodCond = models.BooleanField(null=True)
    ltcControlGoodCond = models.BooleanField(null=True)
    ltcDriveGoodCond = models.BooleanField(null=True)
    animalProtectGoodCond = models.BooleanField(null=True)
    oilPumpFanOp = models.BooleanField(null=True)
    oilLeak = models.CharField(max_length=25, null=True)
    oilContainFreeWater = models.BooleanField(null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    pressReliefGoodCond = models.BooleanField(null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class VacBreakerOutdoor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    counter = models.IntegerField(null=True)
    operatorGoodCond = models.BooleanField(null=True)
    controlCabGoodCond = models.BooleanField(null=True)
    operatorCharged = models.BooleanField(null=True)
    standGoodCond = models.BooleanField(null=True)
    groundGoodCond = models.BooleanField(null=True)
    breakerHousingGoodCond = models.BooleanField(null=True)
    bushings = models.CharField(max_length=25, null=True)
    connectionsGoodCond = models.BooleanField(null=True)
    animalProtectGoodCond = models.BooleanField(null=True)
    potheadGoodCond = models.BooleanField(null=True)
    surgeArrestors = models.CharField(max_length=25, null=True)
    overallEquipCond = models.CharField(max_length=50, null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection
    
    
class MotorOperatedLoadBreak(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspection = models.ForeignKey(
        Inspection,
        verbose_name=('Inspection'),
        on_delete=models.CASCADE
    )
    loadBreaksGoodCond = models.BooleanField(null=True)
    insulatorCond = models.CharField(max_length=25, null=True)
    operatorGoodCond = models.BooleanField(null=True)
    controlCabGoodCond = models.BooleanField(null=True)
    statusCorrectControl = models.BooleanField(null=True)
    groundIntact = models.BooleanField(null=True)
    counter = models.IntegerField(null=True)
    opsSinceLastIns = models.IntegerField(null=True)
    countRoll = models.BooleanField(null=True)
    comment = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return self.inspection