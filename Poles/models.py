from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField(default=timezone.datetime.now())
    author = models.ForeignKey(User, on_delete=0)
    vote_total = models.IntegerField(default=1)

    # def __init__(self, *args, **kwargs):
    #     print("hello")
    #     super(Post,self).__init__(*args, **kwargs)

    #def __unicode__(self):
