from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField()

    def __str__(self):
        return self.title
