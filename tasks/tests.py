from django.test import TestCase
from django.test import Client
from .models import Task
from .models import Profile
from django.contrib.auth.models import User
from django.urls import reverse

class TaskModelTestCase(TestCase):
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

    def test_create_task(self):
        task = Task.objects.create(
            title='New Task',
            description='This is a new task',
            due_date='2023-08-01',
            status='TO_DO',
            profile=self.profile
        )
        self.assertEqual(task.title, 'New Task')
        self.assertEqual(task.description, 'This is a new task')
        self.assertEqual(task.due_date, '2023-08-01')
        self.assertEqual(task.status, 'TO_DO')
        self.assertEqual(task.profile, self.profile)
        self.assertEqual(Task.objects.count(), 3)

    def test_read_task(self):
        task = Task.objects.get(id=self.task1.id)
        self.assertEqual(task.title, 'Task 1')
        self.assertEqual(task.description, 'This is the first task')
        self.assertEqual(str(task.due_date), '2023-06-30')
        self.assertEqual(task.status, 'TO_DO')
        self.assertEqual(task.profile, self.profile)

    def test_update_task(self):
        task = Task.objects.get(id=self.task1.id)
        task.title = 'Updated Task'
        task.description = 'This task has been updated'
        task.due_date = '2023-07-20'
        task.status = 'IN_PROGRESS'
        task.save()

        updated_task = Task.objects.get(id=self.task1.id)
        self.assertEqual(updated_task.title, 'Updated Task')
        self.assertEqual(updated_task.description, 'This task has been updated')
        self.assertEqual(str(updated_task.due_date), '2023-07-20')
        self.assertEqual(updated_task.status, 'IN_PROGRESS')
        self.assertEqual(updated_task.profile, self.profile)

    def test_delete_task(self):
        task = Task.objects.get(id=self.task1.id)
        task.delete()
        self.assertEqual(Task.objects.count(), 1)



class TaskURLTestCase(TestCase):
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

    def test_create_task_url(self):
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)

    def test_delete_task_url(self):
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('delete_task', args=[self.task1.id]))
        self.assertEqual(response.status_code, 200)  
        response = client.post(reverse('delete_task', args=[self.task1.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deletion

    def test_edit_task_url(self):
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('edit_task', args=[self.task1.id]))
        self.assertEqual(response.status_code, 200)

    def test_show_task_url(self):
        client = Client()
        client.login(username='testuser', password='testpass')
        response = client.get(reverse('show_task', args=[self.task1.id]))
        self.assertEqual(response.status_code, 200)
