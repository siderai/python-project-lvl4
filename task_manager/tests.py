from django.test import RequestFactory, TestCase
from .views import *


# c = Client()
# # c.login(username='fred', password='secret')


# What do I test?
# Response statuses
# Db operations (crud, models)


class BaseTest(TestCase):
    def static_home_page_is_ok():
        request = RequestFactory().get('/')
        view = Index()
        view.setup(request)





class UserTest(TestCase):
    def set_up(self):
        self.user = get_user_model().objects.create_user(first_name='A', last_name='Z', username='test', password='12test12')
        self.user.save()
    
    



# class TaskTest(TestCase):

#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
#         self.user.save()
#         self.timestamp = date.today()
#         self.task = Task(user=self.user,
#                          description='description',
#                          due=self.timestamp + timedelta(days=1))
#         self.task.save()

#     def tearDown(self):
#         self.user.delete()

#     def test_read_task(self):
#         self.assertEqual(self.task.user, self.user)
#         self.assertEqual(self.task.description, 'description')
#         self.assertEqual(self.task.due, self.timestamp + timedelta(days=1))

#     def test_update_task_description(self):
#         self.task.description = 'new description'
#         self.task.save()
#         self.assertEqual(self.task.description, 'new description')

#     def test_update_task_due(self):
#         self.task.due = self.timestamp + timedelta(days=2)
#         self.task.save()
#         self.assertEqual(self.task.due, self.timestamp + timedelta(days=2))
