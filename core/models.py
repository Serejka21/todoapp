from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name_plural = "Tags"
        verbose_name = "Tag"

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self):
        return self.task_name
