from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path

from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
                  path('', include(router.urls)),
                  re_path(r'^auth/', include('djoser.urls.authtoken')),
              ] + staticfiles_urlpatterns()
