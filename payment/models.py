from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):
    date_of_payment = models.DateTimeField(auto_now_add=True, verbose_name='date_of_payment')
    course_paid = models.ForeignKey('course.Course', **NULLABLE, on_delete=models.CASCADE, verbose_name='course_paid')
    lesson_paid = models.ForeignKey('course.Lesson', **NULLABLE, on_delete=models.CASCADE, verbose_name='lesson_paid')
    payment_method = models.CharField(max_length=150, choices=[('card', 'Card'), ('transfer', 'Transfer')], verbose_name='payment_method')
    payment_amount = models.IntegerField(verbose_name='payment_amount')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user', related_name='payments')
    stripe_id = models.CharField(max_length=1000, verbose_name='stripe_id')

    def __str__(self):
        return self.course_paid or self.lesson_paid

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'