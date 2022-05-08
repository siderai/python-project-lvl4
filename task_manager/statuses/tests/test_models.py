from django.test import TestCase
from task_manager.statuses.models import Status


class StatusModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Status.objects.create(name='Скоро дедлайн')

    def test_name_max_length(self):
        status = Status.objects.get(id=1)
        max_length = status._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

    def test_object_name(self):
        status = Status.objects.get(id=1)
        expected_object_name = status.name
        self.assertEquals(expected_object_name, str(status))