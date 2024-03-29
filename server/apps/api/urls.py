from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.HourViewSet, base_name='hours')
urlpatterns = router.urls
