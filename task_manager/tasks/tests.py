from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django import test


@test.modify_settings(MIDDLEWARE={'remove': [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]})
class TestTask(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name="Test Status")
        self.obj = Task.objects.create(
            name="Test Task",
            description="Test Description",
            status=self.status,
            author=self.user,
        )

    def test_create_status(self):
        new_obj = Task.objects.create(
            name="Another Test Task",
            description="Another Test Task Description",
            status=self.status,
            author=self.user,
        )

        self.assertEqual(new_obj.name, "Another Test Task")

    def test_read_task(self):
        read_obj = Task.objects.get(id=self.obj.id)

        self.assertEqual(read_obj.name, "Test Task")

    def test_update_task(self):
        self.obj.name = "New Test Task Name"
        self.obj.save()

        updated_obj = Task.objects.get(id=self.obj.id)

        self.assertEqual(updated_obj.name, "New Test Task Name")

    def test_delete_task(self):
        self.obj.delete()

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.obj.id)
