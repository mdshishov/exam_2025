from django.db import models
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = {
        'new': 'New',
        'prg': 'In progress',
        'cmp': 'Completed',
    }

    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_to = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ['-created_at']