from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Task
from tasks.models import Profile
from django.contrib.auth.models import User

class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = Profile.objects.create(user=self.user)
        self.task1 = Task.objects.create(
            title='Task 1',
            description='This is the first task',
            due_date='2023-06-30',
            status='TO_DO',
            profile=self.profile
        )
        self.task2 = Task.objects.create(
            title='Task 2',
            description='This is the second task',
            due_date='2023-07-15',
            status='IN_PROGRESS',
            profile=self.profile
        )

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'New Task',
            'description': 'This is a new task',
            'due_date': '2023-08-01',
            'status': 'TO_DO',
            'profile_id': self.profile.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_retrieve_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        data = {
            'title': 'Updated Task',
            'description': 'This task has been updated',
            'due_date': '2023-07-20',
            'status': 'IN_PROGRESS',
            'profile_id': self.profile.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)
