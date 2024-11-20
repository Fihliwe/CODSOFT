from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='Medium')
    task = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(default='Pending', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task