from django.db import models

# Create your models here.
class Car(models.Model):
    img = models.ImageField(upload_to="image/%Y/%m/%d")
    mark_name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    weight = models.IntegerField()
    price = models.IntegerField()

class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField(max_length=3000)

    class Meta:
        unique_together = ('author', 'text')