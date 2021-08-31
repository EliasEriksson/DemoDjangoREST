from rest_framework import serializers
from .models import Course


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ["code", "name", "progression", "plan"]
