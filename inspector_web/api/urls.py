from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'locations',  views.LocationViewSet)
router.register(r'workgroups', views.WorkGroupViewSet)
router.register(r'jobtitles', views.JobTitleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'regions', views.RegionViewSet)
router.register(r'sizes', views.SizeViewSet)
router.register(r'stations', views.StationsViewSet)
router.register(r'inspectiontype', views.InspectionTypeViewSet)
router.register(r'inspection', views.InspectionViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'equipmenttype', views.EquipmentTypeViewSet)
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'alert', views.AlertViewSet)
router.register(r'mxordertype', views.MxOrderTypeViewSet)
router.register(r'mxorder', views.MxOrderViewSet)
router.register(r'battery', views.BatteryViewSet)
router.register(r'batteryinspection', views.BatteryInspectionViewSet)
router.register(r'building', views.BuildingViewSet)
router.register(r'vacbreakerindoor', views.VacBreakerIndoorViewSet)
router.register(r'vacreclosersinglephase', views.VacRecloserSinglePhaseViewSet)
router.register(r'vacreclosertriplephase', views.VacRecloserTriplePhaseViewSet)
router.register(r'yard', views.YardViewSet)
router.register(r'sf6breaker', views.SF6BreakerViewSet)
router.register(r'station', views.StationViewSet)
router.register(r'capacitorbank', views.CapacitorBankViewSet)
router.register(r'transformer', views.TransformerViewSet)
router.register(r'vacbreakeroutdoor', views.VacBreakerOutdoorViewSet)
router.register(r'motoroperatedloadbreak', views.MotorOperatedLoadBreakViewSet)
router.register(r'circuitswitcher', views.CircuitSwitcherViewSet)
router.register(r'oilbreaker', views.OilBreakerViewSet)
router.register(r'employeetype', views.EmployeeTypeViewSet)
router.register(r'company', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
