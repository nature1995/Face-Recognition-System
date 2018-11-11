from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from rest_framework import routers
from myapp import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register('rasp/dt', views.DtViewSet)
router.register('rasp/tmp', views.TmpViewSet)
router.register('rasp/hmd', views.HmdViewSet)
router.register('rasp/room', views.RoomViewSet)
router.register('rasp/door', views.DoorViewSet)
router.register('rasp/mode', views.ModeViewSet)
router.register('rasp/state', views.StateViewSet)

urlpatterns = [
    path('', include(router.urls), name='rest_api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rasp/', views.rasp, name='rasp'),
]
