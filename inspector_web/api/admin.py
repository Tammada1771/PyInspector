from django.contrib import admin
from .models import Alert, Battery, BatteryInspection, Building, CapacitorBank, Charger, CircuitSwitcher, Company, EmployeeType, Equipment, EquipmentType, Inspection, InspectionType, Location, MotorOperatedLoadBreak, MxOrder, MxOrderType, OilBreaker, Region, SF6Breaker, Size, Station, Stations, Status, Transformer, User, VacBreakerIndoor, VacBreakerOutdoor, VacRecloserSinglePhase, VacRecloserTriplePhase, WorkGroup, JobTitle, Yard

admin.site.register(Location)
admin.site.register(WorkGroup)
admin.site.register(JobTitle)
admin.site.register(User)
admin.site.register(Region)
admin.site.register(Size)
admin.site.register(Stations)
admin.site.register(InspectionType)
admin.site.register(Inspection)
admin.site.register(Status)
admin.site.register(EquipmentType)
admin.site.register(Equipment)
admin.site.register(Alert)
admin.site.register(MxOrderType)
admin.site.register(MxOrder)
admin.site.register(Battery)
admin.site.register(BatteryInspection)
admin.site.register(Building)
admin.site.register(Charger)
admin.site.register(VacBreakerIndoor)
admin.site.register(Yard)
admin.site.register(VacRecloserSinglePhase)
admin.site.register(VacRecloserTriplePhase)
admin.site.register(SF6Breaker)
admin.site.register(Station)
admin.site.register(CapacitorBank)
admin.site.register(Transformer)
admin.site.register(VacBreakerOutdoor)
admin.site.register(MotorOperatedLoadBreak)
admin.site.register(EmployeeType)
admin.site.register(OilBreaker)
admin.site.register(CircuitSwitcher)
admin.site.register(Company)

