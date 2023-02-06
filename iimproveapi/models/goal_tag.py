from django.db import models
from .goal import Goal
from .tag import Tag

class GoalTag(models.Model):

    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
