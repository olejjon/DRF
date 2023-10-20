from datetime import timedelta
from django.utils import timezone


from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Subscription, Course, Lesson
from users.models import User


@shared_task
def send_course_update_email(course_id):
    try:
        course = Course.objects.get(pk=course_id)
        lessons = Lesson.objects.filter(course=course)
        subscriptions = Subscription.objects.filter(course=course, is_active=True)

        email_list = [subscription.user.email for subscription in subscriptions]
        subject = f'Обновился курс: {course.title}'
        message = f'Посмотрите обновление в курсе, обновился урок {lessons}'
        from_email = settings.EMAIL_HOST_USER

        send_mail(subject, message, from_email, email_list, fail_silently=False)
    except Course.DoesNotExist:
        pass


@shared_task
def check_last_login():
    try:
        users = User.objects.all()
        month = timedelta(days=30)
        for user in users:
            if timezone.now() - user.last_login > month:
                user.is_active = False
                user.save()
    except Exception as e:
        return f'Произошла ошибка: {str(e)}'
