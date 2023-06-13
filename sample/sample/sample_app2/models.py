from django.db import models

# Create your models here.


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    about = models.TextField()
    image = models.ImageField(upload_to='gallery1')
    def __str__(self):
        return self.name