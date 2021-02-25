from django.db import models

from django.db import models

class MyModelName(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    objects = None
    category = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='images/')


class Employee(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    sal = models.IntegerField()
