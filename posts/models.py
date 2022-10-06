# Create your models here.
from django.db import models



class Post(models.Model):
    title = models.CharField(('Имя файла'),max_length=20)
    cover = models.FileField((''),upload_to='images/')


def __str__(self):
    return self.title
