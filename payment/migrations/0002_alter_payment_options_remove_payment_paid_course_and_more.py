# Generated by Django 4.2.5 on 2023-09-26 08:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_remove_course_title_course_name'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
        migrations.RemoveField(
            model_name='payment',
            name='paid_course',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='paid_lesson',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_date',
        ),
        migrations.AddField(
            model_name='payment',
            name='course_paid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='course_paid'),
        ),
        migrations.AddField(
            model_name='payment',
            name='date_of_payment',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 9, 26, 8, 21, 34, 711905, tzinfo=datetime.timezone.utc), verbose_name='date_of_payment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='lesson_paid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.lesson', verbose_name='lesson_paid'),
        ),
        migrations.AddField(
            model_name='payment',
            name='stripe_id',
            field=models.CharField(default=datetime.datetime(2023, 9, 26, 8, 21, 45, 875099, tzinfo=datetime.timezone.utc), max_length=300, verbose_name='stripe_id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('cach', 'Cach'), ('transfer', 'Transfer')], max_length=150, verbose_name='payment_method'),
        ),
    ]
