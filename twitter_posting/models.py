from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponse


class TwitterPosts(models.Model):
    twitter_posts = models.CharField(max_length=140)
    user = models.ForeignKey(User)
    date = models.DateTimeField('date created', default=datetime.now)
    hashtag = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.tweet_messages

class Profile(models.Model):
	pass