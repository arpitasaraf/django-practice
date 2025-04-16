from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField()
    author = models.CharField(max_length=100)
    like_count = models.IntegerField(default=0)
    