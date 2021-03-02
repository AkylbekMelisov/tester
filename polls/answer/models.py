from django.db import models


# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=40)
    date_create = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)


class Question(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    true_answer = models.CharField(max_length=40)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)


class ChoiceAnswer(models.Model):
    variance = models.CharField(max_length=40)
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=40)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
