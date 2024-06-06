from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    bio=models.TextField(verbose_name="biography", null=True,blank=True)