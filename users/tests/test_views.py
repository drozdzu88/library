from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from users.models import Profile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'john@example.com',
                                             'johnpassword')
        self.profile = Profile.objects.create(user_id=1)
        self.list_url = reverse('dashboard')
        self.register_url = reverse('register')
        self.edit_url = reverse('edit')

    def test_dashboard_GET(self):
        self.client.login(username='john', password='johnpassword')

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/dashboard.html')

    def test_register_GET(self):

        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')

    def test_edit_GET(self):
        self.client.login(username='john', password='johnpassword')

        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/edit.html')

    def test_register_POST_adds_new_register(self):

        response = self.client.post(self.register_url, {'username': 'john123',
                                                        'email':
                                                            'john@john.com',
                                                        'first_name':
                                                            'johny',
                                                        'password':
                                                            'johnpass'})
        print(response.content)


        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'account/register_done.html')


    def test_edit_POST(self):
        response = self.client.post(self.edit_url, {'first_name': 'john'})

        self.assertEqual(response.status_code, 302)
