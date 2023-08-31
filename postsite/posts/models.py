from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel
# Create your models here.


class Post(TimeStampedModel):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
