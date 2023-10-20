from rest_framework import serializers

from course.models import Subscription, Course
from users.models import User


class SubscriptionSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        fields = ('is_active', 'course', 'user')


class SubscriptionListSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Subscription
        fields = ('is_active', 'course', 'user')


class SubscriptionUpdateSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Subscription
        fields = ('course', 'user')

    def update(self, instance, validated_data):
        instance.is_active = False
        instance.save()
        return instance