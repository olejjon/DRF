from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Lesson, Course
from users.models import User


class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='testuser',
            is_active=True
        )
        self.user.set_password('test')
        self.user.save()
        get_token = reverse('users:token_obtain_pair')
        token_response = self.client.post(path=get_token, data={'email': 'testuser', 'password': 'test'})
        token = token_response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}

        self.course = Course.objects.create(
            name="test_course",
        )


class LessonTestCase(BaseTestCase):

    def test_create(self):
        data = {
            "name": "test",
            "course": 1,
            "link": "https://youtube.com"
        }

        create_lesson = reverse('course:lesson_create')
        response = self.client.post(create_lesson, data, format='json', **self.headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], data['name'])

    def test_retrieve(self):
        Lesson.objects.create(
            id=4,
            name="test",
            course=self.course,
            link="https://youtube.com",
            user_id=self.user.id,
        )
        lesson = reverse('course:get_lesson', kwargs={'pk': 4})
        response = self.client.get(lesson, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        Lesson.objects.create(
            name="test",
            course=self.course,
            link="https://youtube.com",
            user_id=self.user.id,
        )
        data = {
            "name": "test_new",
            "course": 1,
            "link": "https://youtube.com",
            "user_id": self.user.id,
        }

        update_lesson = reverse('course:lesson_update', kwargs={'pk': 2})
        response = self.client.patch(update_lesson, data, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        Lesson.objects.create(
            id=3,
            name="test_delete",
            course=self.course,
            link="https://youtube.com",
            user_id=self.user.id,
        )

        delete_lesson = reverse('course:lesson_delete', kwargs={'pk': 3})
        response = self.client.delete(delete_lesson, format='json', **self.headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
