from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class CustomUser(AbstractUser):

    date_of_birth = models.DateField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.email
