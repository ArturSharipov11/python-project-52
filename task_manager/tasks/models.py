from django.db import models
from task_manager.statuses.models import Status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here
class Task(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='Status')
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(
            get_user_model(),
            on_delete=models.PROTECT,
            related_name='executor',
            default='',
            )
    date_created = models.DateTimeField(auto_now_add=True)