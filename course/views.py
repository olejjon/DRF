from requests import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from course.models import Lesson, Course, Subscription
from course.paginators import LessonPaginator, CoursePaginator
from course.premissions import IsOwner, IsAdmin

from course.serializer.course import CourseSerializer
from course.serializer.lesson import LessonViewSerializer, LessonCreateSerializer
from course.serializer.subscription import SubscriptionUpdateSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsOwner]
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        if self.request.user.has_perm('can_view_courses') or self.request.user.is_superuser:
            queryset = self.queryset
        else:
            queryset = Course.objects.filter(user=self.request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator

    def get_queryset(self):
        if self.request.user.has_perm('can_view_lessons') or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(user=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionUpdateAPIView(generics.UpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionUpdateSerializer
    permission_classes = [IsAuthenticated]