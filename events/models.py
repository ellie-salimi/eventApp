from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default= datetime.now)
    host = models.ForeignKey(User, related_name = 'hosting_events', on_delete = models.CASCADE)
    venue = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    categories = models.ManyToManyField('Category', related_name='events')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return str(self.title).capitalize()


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name).capitalize()