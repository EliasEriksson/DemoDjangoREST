from django.urls import path, re_path
from django.urls import include
from . import views
from rest_framework import routers
from django.http import HttpResponseRedirect
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", obtain_auth_token),
    re_path(r"^auth/$", lambda request: HttpResponseRedirect("login/"), name="api-redirect"),
    path("auth/", include("rest_framework.urls"), name="rest_framework")
]
