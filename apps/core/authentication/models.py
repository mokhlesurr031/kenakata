from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=300)
    contact = models.CharField(max_length=15)
    is_customer = models.BooleanField(default=True)
