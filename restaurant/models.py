from django.db import models
class MyModel(models.Model):
    STATUS = [
        (0, 'Pending'),
        (1, 'In Progress'),
        (2, 'Completed'),
    ]

    status = models.IntegerField(choices=STATUS, default=0)
# Create your models here.

