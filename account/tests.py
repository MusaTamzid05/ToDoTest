from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.profile = Profile.objects.create(user=self.user)

    def test_login(self):
        client = Client()
        
        # Test the login page
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
        # Test the login process
        login_data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        response = client.post(reverse('login'), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        

    def test_logout(self):
        client = Client()
        
        # Log in the user
        client.login(username='testuser', password='testpass')
        
        # Test the logout process
        response = client.post(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
        
