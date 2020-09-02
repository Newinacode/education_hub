from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Feedback(models.Model):
    '''
    Main model for our feedback that is going to be provided by the user
    '''
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
