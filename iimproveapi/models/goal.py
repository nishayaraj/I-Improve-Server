from django.db import models
from .user import User

class Goal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    due = models.DateField()

    @property
    def tags_on_goal(self):
        """using the decorator to get tags on goal
        """
        return self.__tags_on_goal

    @tags_on_goal.setter
    def tags_on_goal(self, value):
        self.__tags_on_goal=value

    # @property
    # def key_metrics_on_goal(self):
    #     """using the decorator to access and set key metrics in goal
    #     """
    #     return self.__key_metrics_on_goal

    # @key_metrics_on_goal.setter
    # def key_metrics_on_goal(self, value):
    #     self.__key_metrics_on_goal=value
