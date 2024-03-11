from django.test import TestCase, Client
from django.urls import reverse

from core.models import Tag, Task


class DashboardViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            task_name="Test Task",
            description="Test Description",
            deadline="2022-12-31",
            done=False,
        )
        self.task.tag.add(self.tag)

    def test_task_list_view(self):
        response = self.client.get(reverse("core:task-list"))
        self.assertEqual(response.status_code, 200)

    def test_tags_view(self):
        response = self.client.get(reverse("core:tag-list"))
        self.assertEqual(response.status_code, 200)

    def test_update_task_view(self):
        test_task_name = "Task"
        response = self.client.post(
            reverse("core:task-edit", kwargs={"pk": self.task.id}),
            data={"task_name": test_task_name},
        )
        self.assertEqual(response.status_code, 200)

    def test_update_tag_view(self):
        test_tag_name = "EditTag"
        response = self.client.post(
            reverse("core:tag-edit", kwargs={"pk": self.tag.id}),
            data={"project_name": test_tag_name},
        )
        self.assertEqual(response.status_code, 200)
