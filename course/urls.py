from django.urls import path

from course.views import SubscriptionCreateAPIView, SubscriptionUpdateAPIView, CourseViewSet, LessonCreateAPIView, \
    LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView

from rest_framework.routers import DefaultRouter
from course.apps import CourseConfig

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='get_lesson'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('subscription', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/update/<int:pk>', SubscriptionUpdateAPIView.as_view(), name='subscription_destroy'),
] + router.urls

# router = DefaultRouter()
# router.register(r'lesson', LessonViewSet, basename='lessons')
#
#
# urlpatterns = [
#                 path('course/create/', CourseCreateAPIView.as_view(), name='create'),
#                 path('course/', CourseListAPIView.as_view(), name='list'),
#                 path('course/<int:pk>', CourseRetrieveAPIView.as_view(), name='retrieve'),
#                 path('course/update/<int:pk>', CourseUpdateAPIView.as_view(), name='update'),
#                 path('course/delete/<int:pk>', CourseDestroyAPIView.as_view(), name='delete'),
#                 path('subscription', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
#                 path('subscription/update/<int:pk>', SubscriptionUpdateAPIView.as_view(),
#                        name='subscription_destroy'),
#               ] + router.urls
