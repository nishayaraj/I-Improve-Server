from django.db import models
from .user import User
from .goal import Goal

class Retro(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    went_well = models.TextField(max_length=500)
    to_improve = models.TextField(max_length=500)
    action_item = models.TextField(max_length=500)
    date = models.DateField()
    status = models.BooleanField()
