from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import dashboard, register, edit


class TestUrls(SimpleTestCase):

    def test_dashboard_url_is_resolverd(self):
        url = reverse('dashboard')
        print(resolve(url))
        self.assertEqual(resolve(url).func, dashboard)

    def test_register_url_is_resolverd(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, register)

    def test_edit_url_is_resolverd(self):
        url = reverse('edit')
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit)

