from django.db.models import fields
from rest_framework import serializers
from .models import Alert, Battery, BatteryInspection, Building, CapacitorBank, Charger, CircuitSwitcher, Company, EmployeeType, Equipment, EquipmentType, Inspection, InspectionType, Location, MotorOperatedLoadBreak, MxOrder, MxOrderType, OilBreaker, SF6Breaker, Stations, Status, Transformer, VacBreakerIndoor, VacBreakerOutdoor, VacRecloserSinglePhase, VacRecloserTriplePhase, WorkGroup, JobTitle, User, Region, Size, Station, Yard



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
        
        
class StationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stations
        fields = ('id', 'name', 'region', 'numInspections', 'company', 'size')
        
        
class InspectionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InspectionType
        fields = ('id', 'name')
        
        
class InspectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inspection
        fields = ('id', 'startdate', 'enddate', 'duration', 'station', 'employee', 'inspectionType')
       

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')
        
        
class EquipmentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ('id', 'name')
        
        
class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'equipmentType', 'equipmentClass', 'manufacturer', 'model', 'serialNumber', 'equipmentNumber', 'station', 'voltage', 'equipmentPostion', 'region')
        
        
class AlertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alert
        fields = ('id', 'date', 'alerter', 'alerted', 'description', 'status', 'equipment', 'station')
        
        
class MxOrderTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MxOrderType
        fields = ('id', 'name')
        
        
class MxOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MxOrder
        fields = ('id', 'type', 'issuer', 'date', 'station', 'equipment')
        
        
class BatterySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Battery
        fields = ('id', 'inspection', 'equipment', 'cellElectrolyteLevel', 'cellFreeLeaks', 'postStrapFreeCorro', 'overallEquipCond', 'comment')
        
        
class BatteryInspectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BatteryInspection
        fields = ('id', 'inspection', 'equipment', 'tempBatRoom', 'ventChecked', 'rackCond', 'cellElectrolyteLevel', 'cellFreeLeaks', 'deminWaterAdded', 'postStrapFreeCorro', 'positiveGround', 'negativeGround', 'vlaGroundTestRatio', 'floatVolts', 'floatAmps', 'ampUnits', 'charger1Volt', 'charger1Amp', 'charger2Volt', 'charger2Amp', 'charger3Volt', 'charger3Amp', 'overallEquipCond', 'comment')
        
        
class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = ('id', 'inspection', 'equipment', 'groundIntact', 'phonelineClear', 'operatingInstrct', 'onelineDia', 'spareFuseQntOk', 'stationInfo', 'acdcPanelGoodCond', 'acdcPanelFlagFree', 'relatPanelGoodCond', 'indicateLightsSvcPanel', 'hvacFanOp', 'toolEquipGoodCond', 'fireExtCharged', 'fireExtTagSign', 'exitLightOp', 'thermSetCool75Heat55', 'siliconWipeStock', 'operatingInstructDate', 'floorCleanGoodCond', 'freeRodent', 'overallEquipCond', 'comment')
        
        
class ChargerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Charger
        fields = ('id', 'inspection', 'equipment', 'volt', 'amp', 'noGroundPres', 'overallEquipCond', 'comment')
        
        
class VacBreakerIndoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VacBreakerIndoor
        fields = ('id', 'inspection', 'equipment', 'heaterCond', 'counter', 'operatorCharged', 'breakerCubGoodCon', 'overallEquipCond', 'comment')
        
        
class VacRecloserSinglePhaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VacRecloserSinglePhase
        fields = ('id', 'inspection', 'equipment', 'surgerArrestors', 'counter', 'bushings', 'connectionsGoodCond', 'tankGoodCond', 'oilLeaks', 'animalProtectGoodCond', 'potheadGoodCond', 'overallEquipCond', 'comment')
        
        
class VacRecloserTriplePhaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VacRecloserTriplePhase
        fields = ('id', 'inspection', 'equipment', 'surgerArrestors', 'countera', 'counterb', 'counterc', 'bushings', 'connectionsGoodCond', 'tankGoodCond', 'oilLeaks', 'animalProtectGoodCond', 'potheadGoodCond', 'overallEquipCond', 'comment')
        
        
class YardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Yard
        fields = ('id', 'inspection', 'equipment', 'weather', 'landscapingGoodCond', 'gatesDoorsGoodCond', 'groundsGateIntact', 'perimeterGoodCond', 'noHoleFabric', 'rampartGoodCond', 'groundsIntact40ft', 'gapsLess6in', 'warningSignGate', 'exterLightGoodCond', 'freeVegInside', 'freeLiter', 'freeItemsStored', 'cableTrenchGoodCond', 'lightningMastGoodCond', 'stoneGoodCond', 'overallEquipCond', 'climbingAssist4ft', 'comment')
        
              
class SF6BreakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SF6Breaker
        fields = ('id', 'inspection', 'equipment', 'counter', 'operatorGoodCond', 'controlCabGoodCond', 'gasPressInLimit', 'gasPress', 'standGoodCond', 'busings', 'connectionsGoodCond', 'overallEquipCond', 'potheadGoodCond', 'comment')
        
        
class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'inspection', 'equipment', 'conductorGoodCond', 'freeBirdInsect', 'disconnectSwitchGoodCond', 'insulatorGoodCond', 'ptsGoodCond', 'ptFusesGoodCond', 'auxTRFGoodCond', 'auxTRFFusesGoodCond', 'animalProtectGoodCond', 'groundIntact', 'overallEquipCond', 'ctGoodCond', 'comment')
        
        
class CapacitorBankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CapacitorBank
        fields = ('id', 'inspection', 'equipment', 'freeBulgedCans', 'signsPerimeter', 'pdptctGoodCond', 'fusesIntact', 'surgeArrestors', 'overallEquipCond', 'comment')
        
        
class TransformerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transformer
        fields = ('id', 'inspection', 'equipment', 'counter', 'didCountRoll', 'lowerDrag', 'raiseDrag', 'oilLevel', 'currentWindTemp', 'maxWindTemp', 'currentTopTemp', 'maxTopTemp', 'mainTankPres', 'n2BottlePress', 'n2SysGoodCond', 'ltcOilLevel', 'dessicantColor', 'hvBushCond', 'lvBushCond', 'surgeArrestorCond', 'pressReliefNotAct', 'suddenPressValveOpen', 'heatersWorkProp', 'cabClean', 'radiatorGoodCond', 'ltcControlGoodCond', 'ltcDriveGoodCond', 'animalProtectGoodCond', 'oilPumpFanOp', 'oilLeak', 'oilContainFreeWater', 'overallEquipCond', 'pressReliefGoodCond', 'comment')
        
        
class VacBreakerOutdoorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VacBreakerOutdoor
        fields = ('id', 'inspection', 'equipment', 'counter', 'operatorGoodCond', 'controlCabGoodCond', 'operatorCharged', 'standGoodCond', 'groundGoodCond', 'breakerHousingGoodCond', 'bushings', 'connectionsGoodCond', 'animalProtectGoodCond', 'potheadGoodCond', 'surgeArrestors', 'overallEquipCond', 'comment')
        
        
class MotorOperatedLoadBreakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MotorOperatedLoadBreak
        fields = ('id', 'inspection', 'equipment', 'loadBreaksGoodCond', 'insulatorCond', 'operatorGoodCond', 'controlCabGoodCond', 'statusCorrectControl', 'groundIntact', 'counter', 'opsSinceLastIns', 'countRoll', 'comment')


class OilBreakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OilBreaker
        fields = ('id', 'inspection', 'equipment', 'operatorCounter', 'compressorHours', 'hydraulicPress', 'airPress', 'moistureDrain', 'tankOilLevel', 'bushingOilLevel', 'freeOilSheen', 'oilLeaks', 'overallPhysCond', 'comment')
    
    
class EmployeeTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ('id', 'name')
        
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')
        
        
class CircuitSwitcherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CircuitSwitcher
        fields = ('id', 'name', 'equipment', 'counter', 'operatorGoodCond', 'gasPressProperPress', 'controlCabGoodCond', 'standGoodCond', 'interrupterCond', 'insulatorFreeLeak', 'disconnectSwitchGoodCond', 'equipmentLabelProp', 'overallEquipCond', 'foundationGoodCond', 'paintCond', 'comment')
        
        