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

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
