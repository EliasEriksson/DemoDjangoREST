from django.http import HttpRequest, HttpResponse
from .serializers import Course, CoursesSerializer
from rest_framework import viewsets
from .models import Course
from .serializers import CoursesSerializer
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

