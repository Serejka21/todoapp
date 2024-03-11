from django.test import TestCase


from core.models import Tag, Task


class TagModelTest(TestCase):
    def test_str_method(self):
        position = Tag.objects.create(name="Test")
        self.assertEqual(str(position), "Test")


class TaskModelTest(TestCase):
    def test_str_method(self):
        task_type = Task.objects.create(task_name="Test Task")
        self.assertEqual(str(task_type), "Test Task")
