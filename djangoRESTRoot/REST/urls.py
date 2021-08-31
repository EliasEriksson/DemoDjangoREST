from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls"), name="rest_framework")
]
