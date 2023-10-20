from datetime import timezone

from rest_framework import serializers

from course.models import Lesson, Course
from course.validators import UrlValidator
from users.models import User


class LessonCreateSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    link = serializers.URLField(validators=[UrlValidator()])

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course',)


class LessonViewSerializer(LessonCreateSerializer):
    course = serializers.StringRelatedField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course', 'user')

