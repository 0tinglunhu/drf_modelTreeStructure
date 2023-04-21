from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet)
router.register(r'component', views.ComponentViewSet)
router.register(r'sensor', views.SensorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
]