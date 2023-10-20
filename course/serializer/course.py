from datetime import timezone

from rest_framework import serializers
from course.tasks import send_course_update_email
from course.models import Course, Subscription
from course.serializer.lesson import LessonViewSerializer
from course.serializer.subscription import SubscriptionListSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscription = SubscriptionListSerializer(read_only=True, many=True, source='course_subscriptions')
    lessons = LessonViewSerializer(read_only=True, many=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'image', 'lessons_count', 'lessons', 'subscription')

    def update(self, instance, validated_data):
        subscription = Subscription.objects.filter(course_id=instance.id, is_active=True)
        if subscription:
            instance.updated_at = timezone.now()
        send_course_update_email.delay(instance.id)

        instance.save()
        return super().update(instance, validated_data)