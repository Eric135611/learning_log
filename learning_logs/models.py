from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    #the topic of users' learning
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    

class Entry(models.Model):
    #the specific knowledge about a topic of users' learning
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #return str expression of model
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:50] + '...'