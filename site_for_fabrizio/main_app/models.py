from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200, blank=True)
    text1 = models.TextField(max_length=700)
    text2 = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name='Image')


class Client(models.Model):
    info = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.info
# Create your models here.
