from api import views
from rest_framework import routers
from django.urls import path
from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewsets)
router.register(r'events', views.EventViewsets)
router.register(r'members', views.MemberViewsets)
router.register(r'comments', views.CommentViewset)
router.register(r'users', views.UserViewsets)
router.register(r'profile', views.UserProfileViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url("authenticate/", views.CustomObtainAuthToken.as_view())

]