from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    chanson = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True, blank=True)
