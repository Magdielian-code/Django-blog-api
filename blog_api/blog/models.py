from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# This model is for every post on Nome_write
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # To make the post objects more descriptive when printed out
    def __str__(self):
        return self.title