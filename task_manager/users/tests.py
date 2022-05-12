from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from task_manager.tests import LOGIN_URL_NAME


USERS_URL_NAME = reverse('users')
CREATE_USER_URL_NAME = reverse('user_create')
UPDATE_USER_URL_NAME = 'user_update'
DELETE_USER_URL_NAME = 'user_delete'


class UserListViewTest(TestCase):

    @classmethod
    def setUpTestData(cla):
        number_of_users = 5
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123'
            )

    def test_view_uses_correct_template(self):
        response = self.client.get(USERS_URL_NAME)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users.html')

    def test_lists_all_users(self):
        response = self.client.get(USERS_URL_NAME)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['users']) == 5)


class CreateUserViewTest(TestCase):
    number_of_users = 2

    def setUp(self):
        for user_num in range(self.number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

    def test_view_uses_correct_template(self):
        response = self.client.get(CREATE_USER_URL_NAME)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-create.html')

    def test_create(self):
        for user_num in range(self.number_of_users):
            self.assertTrue(User.objects.get(first_name=f'First name {user_num}'))
        self.assertEqual(User.objects.all().count(), 2)


class UpdateUserViewTest(TestCase):

    def setUp(self):
        number_of_users = 2
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(
            reverse(UPDATE_USER_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(LOGIN_URL_NAME))

    def test_redirect_if_logged_in_but_not_passed_test(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(
            reverse(UPDATE_USER_URL_NAME, kwargs={'pk': 2})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(USERS_URL_NAME))

    def test_logged_in_passed_test_uses_correct_template(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(
            reverse(UPDATE_USER_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(str(response.context['user']), 'Username 0')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-update.html')

    def test_update(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.post(
            reverse(UPDATE_USER_URL_NAME, kwargs={'pk': 1}),
            {
                'first_name': 'test',
                'last_name': 'update',
                'username': 'test_update',
                'password1': '123',
                'password2': '123',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(USERS_URL_NAME))
        self.assertEqual(User.objects.get(pk=1).username, 'test_update')


class DeleteUserViewTest(TestCase):

    def setUp(self):
        number_of_users = 2
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(
            reverse(DELETE_USER_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(LOGIN_URL_NAME))

    def test_redirect_if_logged_in_but_not_passed_test(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(
            reverse(DELETE_USER_URL_NAME, kwargs={'pk': 2})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(USERS_URL_NAME))

    def test_logged_in_passed_test_uses_correct_template(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(
            reverse(DELETE_USER_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(str(response.context['user']), 'Username 0')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-delete.html')

    def test_delete(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.post(
            reverse(DELETE_USER_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(USERS_URL_NAME))
        self.assertFalse(User.objects.filter(pk=1))
