from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    first_name = models.CharField(max_length=150,
    editable=False)
    last_name = models.CharField(max_length=150,
    editable=False)
    name = models.CharField(max_length=15, default=False)
    is_host = models.BooleanField(default=False)
    pass

# Create your models here.