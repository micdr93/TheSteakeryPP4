from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
