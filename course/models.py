from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    image = models.ImageField(**NULLABLE, upload_to='courses/', verbose_name='image')
    description = models.TextField(**NULLABLE, verbose_name='description')
    user = models.ForeignKey('users.User', **NULLABLE, on_delete=models.CASCADE, verbose_name='user', related_name='course')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='lesson')
    description = models.TextField(**NULLABLE, verbose_name='description')
    preview = models.ImageField(**NULLABLE, upload_to='lessons', verbose_name='preview')
    link = models.URLField(**NULLABLE, verbose_name='link')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, verbose_name='course', related_name='lessons')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user', related_name='lessons')

    def __str__(self):
        return f'{self.name}{self.course} {self.link}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


class Subscription(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='course_subscriptions')

    def __str__(self):
        return f'{self.user.email} {self.course.title} '

    class Meta:
        verbose_name = 'subscriptions'
        verbose_name_plural = 'subscriptions'