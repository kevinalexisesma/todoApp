from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< Updated upstream
# Create your models here.

=======

# Create your models here.
>>>>>>> Stashed changes

class Profile(AbstractUser):
    bio=models.TextField(verbose_name="biography", null=True,blank=True)