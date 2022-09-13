from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length = 100)
    memo = models.TextField(blank = True)

    # set to the current time
    created = models.DateTimeField(auto_now_add = True)
    completed = models.BooleanField(default = False)

    # user who posted this
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.title