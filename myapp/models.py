from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    image = models.CharField(max_length=20)
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField()

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=150)
