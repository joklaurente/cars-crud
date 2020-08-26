from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return (self.name)