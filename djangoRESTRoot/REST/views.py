from rest_framework import viewsets
from .models import Course
from .serializers import CoursesSerializer
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

