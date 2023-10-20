# Generated by Django 4.2.5 on 2023-09-26 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_remove_course_lessons_remove_lesson_courses_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated'),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=11, verbose_name='price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lessons', to='course.course', verbose_name='course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses', to=settings.AUTH_USER_MODEL, verbose_name='course owner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='courses/previews', verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='video link'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lessons', to=settings.AUTH_USER_MODEL, verbose_name='lesson owner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='lessons/previews', verbose_name='preview'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
