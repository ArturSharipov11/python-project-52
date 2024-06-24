from django.test import TestCase, Client
from django.test.utils import override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings


class UsersTests(TestCase):

    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        cls.user_data = {
            "first_name": "Test",
            "last_name": "User",
            "username": "TestUser",
            "password1": "testing12",
            "password2": "testing12",
        }
        cls.user = get_user_model().objects.create_user(
            username="TestUser", password="testing12"
        )
        cls.user2 = get_user_model().objects.create_user(
            username="TestUser2", password="testing12"
        )

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_registration_GET(self):
        response = self.client.get(reverse("create_user"))
        self.assertEqual(response.status_code, 200)

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_login_GET(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_login_POST(self):
        # Test wrong creds
        response = self.client.post(reverse("login"), {
            "username": "TestUser", "password": "testings"
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

        # Test correct creds
        response = self.client.post(reverse("login"), {
            "username": "TestUser", "password": "testing12"
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_logout_POST(self):
        self.client.login(username="TestUser", password="testing12")
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_update_GET(self):
        url = reverse("update_user", kwargs={"id": self.user.pk})
        url = f"/users/{self.user.pk}/update/"

        # Test without login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/")

        # Test with login
        self.client.login(username="TestUser", password="testing12")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestUser")

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_update_POST(self):
        url = f"/users/{self.user.pk}/update/"
        self.client.login(username="TestUser", password="testing12")

        # Test wrong inputs
        response = self.client.post(url, {
            "first_name": "Test",
            "last_name": "User",
            "username": "TestUser","password2": "testing12",
        })
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "")

        # Test correct inputs
        response = self.client.post(url, {
            "first_name": "Test",
            "last_name": "User",
            "username": "TestUser",
            "password1": "testing12",
            "password2": "testing12",
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Test")

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_delete_GET(self):
        url = f"/users/{self.user.pk}/delete/"

        # Test without login
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # Test attempt to delete wrong user
        self.client.login(username="TestUser", password="testing12")
        url2 = f"/users/{self.user2.pk}/delete/"
        response = self.client.get(url2)
        self.assertEqual(response.status_code, 302)

        # Test with login
        self.client.login(username="TestUser", password="testing12")
        response = self.client.get(url)
        self.assertContains(response, self.user.first_name, status_code=200)

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_delete_POST(self):
        self.client.login(username="TestUser2", password="testing12")
        url = f"/users/{self.user2.pk}/delete/"
        user_pk = self.user2.pk

        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(get_user_model().objects.filter(pk=user_pk).exists())

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_main_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    @override_settings(MIDDLEWARE=[
        m for m in settings.MIDDLEWARE
        if m != 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware'
    ])
    def test_users_index_view(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)
