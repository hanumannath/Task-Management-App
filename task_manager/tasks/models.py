from django.db import models
from django.contrib.auth.models import User

from .constants import TaskType, TaskStatus


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_type = models.CharField(
        max_length=10,
        choices=[(task_type.value, task_type.name.capitalize()) for task_type in TaskType],
        default=TaskType.GENERAL.value
    )
    status = models.CharField(
        max_length=15,
        choices=[(status.value, status.name.capitalize()) for status in TaskStatus],
        default=TaskStatus.PENDING.value
    )
    assigned_users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
