from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tweet(models.Model):
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="author")
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name="liked_by")

class Hashtag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    tweet = models.ManyToManyField(Tweet)

    def __str__(self):
        return self.name
