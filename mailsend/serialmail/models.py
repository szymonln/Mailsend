from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MailProvider(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
