from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AlertSerializer, BatteryInspectionSerializer, BatterySerializer, BuildingSerializer, CapacitorBankSerializer, ChargerSerializer, CircuitSwitcherSerializer, CompanySerializer, EmployeeTypeSerializer, EquipmentSerializer, EquipmentTypeSerializer, InspectionSerializer, InspectionTypeSerializer, LocationSerializer, MotorOperatedLoadBreakSerializer, MxOrderSerializer, MxOrderTypeSerializer, OilBreakerSerializer, SF6BreakerSerializer, StationSerializer, StationsSerializer, StatusSerializer, TransformerSerializer, VacBreakerIndoorSerializer, VacBreakerOutdoorSerializer, VacRecloserSinglePhaseSerializer, VacRecloserTriplePhaseSerializer, WorkGroupSerializer, JobTitleSerializer, UserSerializer, RegionSerializer, SizeSerializer, YardSerializer

from .models import Alert, Battery, BatteryInspection, Building, CapacitorBank, Charger, CircuitSwitcher, Company, EmployeeType, Equipment, EquipmentType, Inspection, InspectionType, Location, MotorOperatedLoadBreak, MxOrder, MxOrderType, OilBreaker, SF6Breaker, Station, Stations, Status, Transformer, VacBreakerIndoor, VacBreakerOutdoor, VacRecloserSinglePhase, VacRecloserTriplePhase, WorkGroup, JobTitle, User, Region, Size, Yard


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


class StationsViewSet(viewsets.ModelViewSet):
    queryset = Stations.objects.all().order_by('name')
    serializer_class = StationsSerializer
    

class InspectionTypeViewSet(viewsets.ModelViewSet):
    queryset = InspectionType.objects.all().order_by('name')
    serializer_class = InspectionTypeSerializer
    
    
class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all().order_by('station')
    serializer_class = InspectionSerializer
    
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all().order_by('name')
    serializer_class = StatusSerializer
    

class EquipmentTypeViewSet(viewsets.ModelViewSet):
    queryset = EquipmentType.objects.all().order_by('name')
    serializer_class = EquipmentTypeSerializer
    
    
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all().order_by('station')
    serializer_class = EquipmentSerializer
    
    
class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by('date')
    serializer_class = AlertSerializer
    
    
class MxOrderTypeViewSet(viewsets.ModelViewSet):
    queryset = MxOrderType.objects.all().order_by('name')
    serializer_class = MxOrderTypeSerializer
    
    
class MxOrderViewSet(viewsets.ModelViewSet):
    queryset = MxOrder.objects.all().order_by('station')
    serializer_class = MxOrderSerializer
    
    
class BatteryViewSet(viewsets.ModelViewSet):
    queryset = Battery.objects.all().order_by('inspection')
    serializer_class = BatterySerializer
    
    
class BatteryInspectionViewSet(viewsets.ModelViewSet):
    queryset = BatteryInspection.objects.all().order_by('inspection')
    serializer_class = BatteryInspectionSerializer
    
    
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all().order_by('inspection')
    serializer_class = BuildingSerializer
    
    
class ChargerViewSet(viewsets.ModelViewSet):
    queryset = Charger.objects.all().order_by('inspection')
    serializer_class = ChargerSerializer
    
    
class VacBreakerIndoorViewSet(viewsets.ModelViewSet):
    queryset = VacBreakerIndoor.objects.all().order_by('inspection')
    serializer_class = VacBreakerIndoorSerializer
       
    
class VacRecloserSinglePhaseViewSet(viewsets.ModelViewSet):
    queryset = VacRecloserSinglePhase.objects.all().order_by('inspection')
    serializer_class = VacRecloserSinglePhaseSerializer
    
    
class VacRecloserTriplePhaseViewSet(viewsets.ModelViewSet):
    queryset = VacRecloserTriplePhase.objects.all().order_by('inspection')
    serializer_class = VacRecloserTriplePhaseSerializer
    
    
class YardViewSet(viewsets.ModelViewSet):
    queryset = Yard.objects.all().order_by('inspection')
    serializer_class = YardSerializer
    
    
class SF6BreakerViewSet(viewsets.ModelViewSet):
    queryset = SF6Breaker.objects.all().order_by('inspection')
    serializer_class = SF6BreakerSerializer
    
    
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all().order_by('inspection')
    serializer_class = StationSerializer
    

class CapacitorBankViewSet(viewsets.ModelViewSet):
    queryset = CapacitorBank.objects.all().order_by('inspection')
    serializer_class = CapacitorBankSerializer
    
    
class VacBreakerOutdoorViewSet(viewsets.ModelViewSet):
    queryset = VacBreakerOutdoor.objects.all().order_by('inspection')
    serializer_class = VacBreakerOutdoorSerializer
    
    
class MotorOperatedLoadBreakViewSet(viewsets.ModelViewSet):
    queryset = MotorOperatedLoadBreak.objects.all().order_by('inspection')
    serializer_class = MotorOperatedLoadBreakSerializer
    
    
class TransformerViewSet(viewsets.ModelViewSet):
    queryset = Transformer.objects.all().order_by('inspection')
    serializer_class = TransformerSerializer
    
    
class OilBreakerViewSet(viewsets.ModelViewSet):
    queryset = OilBreaker.objects.all().order_by('inspection')
    serializer_class = OilBreakerSerializer
    

class EmployeeTypeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeType.objects.all().order_by('name')
    serializer_class = EmployeeTypeSerializer
    
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    
    
class CircuitSwitcherViewSet(viewsets.ModelViewSet):
    queryset = CircuitSwitcher.objects.all().order_by('inspection')
    serializer_class = CircuitSwitcherSerializer