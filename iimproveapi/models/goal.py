from django.db import models
from .user import User

class Goal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    due = models.DateField()
