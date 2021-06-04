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
router.register(r'stationss', views.StationsViewSet)
router.register(r'inspectiontypes', views.InspectionTypeViewSet)
router.register(r'inspections', views.InspectionViewSet)
router.register(r'statuss', views.StatusViewSet)
router.register(r'equipmenttypes', views.EquipmentTypeViewSet)
router.register(r'equipments', views.EquipmentViewSet)
router.register(r'alerts', views.AlertViewSet)
router.register(r'mxordertypes', views.MxOrderTypeViewSet)
router.register(r'mxorders', views.MxOrderViewSet)
router.register(r'batterys', views.BatteryViewSet)
router.register(r'batteryinspections', views.BatteryInspectionViewSet)
router.register(r'buildings', views.BuildingViewSet)
router.register(r'vacbreakerindoors', views.VacBreakerIndoorViewSet)
router.register(r'vacreclosersinglephases', views.VacRecloserSinglePhaseViewSet)
router.register(r'vacreclosertriplephases', views.VacRecloserTriplePhaseViewSet)
router.register(r'yards', views.YardViewSet)
router.register(r'sf6breakers', views.SF6BreakerViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'capacitorbanks', views.CapacitorBankViewSet)
router.register(r'transformers', views.TransformerViewSet)
router.register(r'vacbreakeroutdoors', views.VacBreakerOutdoorViewSet)
router.register(r'motoroperatedloadbreaks', views.MotorOperatedLoadBreakViewSet)
router.register(r'circuitswitchers', views.CircuitSwitcherViewSet)
router.register(r'oilbreakers', views.OilBreakerViewSet)
router.register(r'employeetypes', views.EmployeeTypeViewSet)
router.register(r'companys', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
