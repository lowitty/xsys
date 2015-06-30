from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_age = models.IntegerField(default=20)
    pub_date = models.DateTimeField('date joined')
    
    def __unicode__(self):
        return self.user_name
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Node(models.Model):
    user = models.ForeignKey(User)
    label = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.label