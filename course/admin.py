from django.contrib import admin

from course.models import Course
from course.models import Lesson

admin.site.register(Course)
admin.site.register(Lesson)
