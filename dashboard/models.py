from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class AnonMessage(models.Model):
    user = models.ForeignKey(User,models.CASCADE,related_name='messages')
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    