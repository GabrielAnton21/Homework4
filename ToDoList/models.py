from django.db import models


# Create your models here.

class Tasks(models.Model):
    task = models.CharField(max_length=200, default="Add Task")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
