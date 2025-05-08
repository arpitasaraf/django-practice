from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, # jis model ki primary key attach karni hai uska Model class.
        on_delete=models.CASCADE, # agar user delete hua to uske sarey blogs delete ho jayenge.
        default= None,
    )

    def __str__(self):
        return self.title
