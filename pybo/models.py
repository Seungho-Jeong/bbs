from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    subject    = models.CharField(max_length=200)
    content    = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    voter      = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question   = models.ForeignKey(Question, on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    voter      = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    question   = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer     = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)