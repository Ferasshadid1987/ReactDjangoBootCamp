from api import views
from rest_framework import routers
from django.urls import path
from django.conf.urls import url, include

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewsets)
router.register(r'events', views.EventViewsets)

urlpatterns = [
    url(r'^', include(router.urls)),

]