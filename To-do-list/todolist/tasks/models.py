from django.db import models

# Create your models here.

class Task(models.Model):
    tasks = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tasks