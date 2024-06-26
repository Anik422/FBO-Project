from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, unique=True, db_index=True)

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
