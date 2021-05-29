from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'locations',  views.LocationViewSet)
router.register(r'workgroups', views.WorkGroupViewSet)
router.register(r'jobtitles', views.JobTitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework'))
]
