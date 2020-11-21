from django.db import models
from django.contrib.auth.models import User


class MyPoll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count = models.IntegerField(default=0)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count