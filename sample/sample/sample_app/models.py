from django.db import models

# Create your models here.


class Celeb(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    info = models.TextField()
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

