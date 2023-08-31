from django.contrib.auth.models import User

from django.db import models
from .core import get_profile_upload_path
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=get_profile_upload_path, blank=True)