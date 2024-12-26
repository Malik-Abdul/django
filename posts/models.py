from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75) # explore: https://docs.djangoproject.com/en/5.1/topics/db/models/#field-types
    body = models.TextField()
    slug = models.SlugField(default='default-slug')
    date = models.DateTimeField(auto_now_add=True) # will automatically date time stamp when user add data in this table

    def __str__(self):
        return self.title