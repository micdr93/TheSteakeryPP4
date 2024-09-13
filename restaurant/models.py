from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
slug = models.SlugField(max_length=200, unique=True)
author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
content = models.TextField()
created_on = models.DateTimeField(auto_now_add=True)
status = models.IntegerField(choices=STATUS, default=0)
STATUS = ((0, "Draft"), (1, "Published"))

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description available') 
    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description available')

    def __str__(self):
        return self.name

class Booking(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.resource.name} booked by {self.user.username}'

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
