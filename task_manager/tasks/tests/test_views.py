from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


LOGIN_URL_NAME = reverse('login')
TASKS_URL_NAME = reverse('tasks')
CREATE_TASK_URL_NAME = reverse('task_create')
TAKS_DETAIL_URL_NAME = 'task_detail'
UPDATE_TASK_URL_NAME = 'task_update'
DELETE_TASK_URL_NAME = 'task_delete'


class TaskListViewTest(TestCase):

    def setUp(self):
        number_of_users = 2
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

        number_of_statuses = 2
        for status_num in range(number_of_statuses):
            Status.objects.create(name=f'Status {status_num}')

        number_of_labels = 2
        for labels_num in range(number_of_labels):
            Label.objects.create(name=f'Label {labels_num}')

        number_of_tasks = 5
        for task_num in range(number_of_tasks):
            num1 = 1 if task_num < 3 else 2
            num2 = 2 if task_num < 3 else 1
            a = Task.objects.create(
                name=f'Task {task_num}',
                description=f'Task description {task_num}',
                status=Status.objects.get(pk=num1),
                executor=User.objects.get(pk=num2),
                author=User.objects.get(pk=num1)
            )
            a.labels.add(Label.objects.get(pk=num1))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(TASKS_URL_NAME)
        self.assertEqual(
            str(response.context['user']),
            'Username 0'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task-list.html')
        self.assertEqual(response.context['tasks'].count(), 5)

    def test_filter(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(TASKS_URL_NAME, {'executor': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['tasks'].count(), 2)
        response = self.client.get(
            TASKS_URL_NAME,
            {'self_tasks': 'on'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['tasks'].count(), 3)
        response = self.client.get(TASKS_URL_NAME, {'status': 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['tasks'].count(), 3)
        response = self.client.get(TASKS_URL_NAME, {'labels': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['tasks'].count(), 2)


class TaskDetailViewTest(TestCase):

    def setUp(self):
        number_of_users = 2
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

        number_of_statuses = 1
        for status_num in range(number_of_statuses):
            Status.objects.create(name=f'Status {status_num}')

        number_of_labels = 1
        for labels_num in range(number_of_labels):
            Label.objects.create(name=f'Label {labels_num}')

        number_of_tasks = 1
        for task_num in range(number_of_tasks):
            a = Task.objects.create(
                name=f'Task {task_num}',
                description=f'Task description {task_num}',
                status=Status.objects.get(pk=1),
                executor=User.objects.get(pk=2),
                author=User.objects.get(pk=1)
            )
            a.labels.add(Label.objects.get(pk=1))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(
            reverse(TAKS_DETAIL_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(
            str(response.context['user']),
            'Username 0'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task-detail.html')


class CreateTaskViewTest(TestCase):

    def setUp(self):
        number_of_users = 2
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

        number_of_statuses = 1
        for status_num in range(number_of_statuses):
            Status.objects.create(name=f'Status {status_num}')

        number_of_labels = 1
        for labels_num in range(number_of_labels):
            Label.objects.create(name=f'Label {labels_num}')

        number_of_tasks = 2
        for task_num in range(number_of_tasks):
            a = Task.objects.create(
                name=f'Task {task_num}',
                description=f'Task description {task_num}',
                status=Status.objects.get(pk=1),
                executor=User.objects.get(pk=2),
                author=User.objects.get(pk=1)
            )
            a.labels.add(Label.objects.get(pk=1))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.get(CREATE_TASK_URL_NAME)
        self.assertEqual(
            str(response.context['user']),
            'Username 0'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task-create.html')

    def test_create(self):
        self.client.login(username='Username 0', password='123')
        self.assertTrue(Task.objects.get(name='Task 0'))
        self.assertTrue(Task.objects.get(name='Task 1'))
        self.assertEqual(Task.objects.all().count(), 2)


class UpdateTaskViewTest(TestCase):

    def setUp(self):
        number_of_users = 2
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

        number_of_statuses = 1
        for status_num in range(number_of_statuses):
            Status.objects.create(name=f'Status {status_num}')

        number_of_labels = 1
        for labels_num in range(number_of_labels):
            Label.objects.create(name=f'Label {labels_num}')

        number_of_tasks = 1
        for task_num in range(number_of_tasks):
            a = Task.objects.create(
                name=f'Task {task_num}',
                description=f'Task description {task_num}',
                status=Status.objects.get(pk=1),
                executor=User.objects.get(pk=2),
                author=User.objects.get(pk=1)
            )
            a.labels.add(Label.objects.get(pk=1))

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='Username 0', password='123')
        self.assertTrue(Task.objects.get(name='Task 0'))
        response = self.client.get(
            reverse(UPDATE_TASK_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(
            str(response.context['user']),
            'Username 0'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task-update.html')


class DeleteTaskViewTest(TestCase):

    def setUp(self):
        number_of_users = 3
        for user_num in range(number_of_users):
            User.objects.create_user(
                first_name=f'First name {user_num}',
                last_name=f'Last name {user_num}',
                username=f'Username {user_num}',
                password='123',
            )

        number_of_statuses = 1
        for status_num in range(number_of_statuses):
            Status.objects.create(name=f'Status {status_num}')

        number_of_labels = 1
        for labels_num in range(number_of_labels):
            Label.objects.create(name=f'Label {labels_num}')

        number_of_tasks = 2
        for task_num in range(number_of_tasks):
            a = Task.objects.create(
                name=f'Task {task_num}',
                description=f'Task description {task_num}',
                status=Status.objects.get(pk=1),
                executor=User.objects.get(pk=2),
                author=User.objects.get(pk=1)
            )
            a.labels.add(Label.objects.get(pk=1))

    def test_redirect_if_logged_in_but_not_passed_test(self):
        self.client.login(username='Username 1', password='123')
        response = self.client.get(
            reverse(DELETE_TASK_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(TASKS_URL_NAME))

    def test_delete(self):
        self.client.login(username='Username 0', password='123')
        response = self.client.post(
            reverse(DELETE_TASK_URL_NAME, kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(TASKS_URL_NAME))
        self.assertFalse(Task.objects.filter(pk=1))
