from django.db import models
from .goal import Goal

class KeyMetrics(models.Model):

    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.BooleanField()
