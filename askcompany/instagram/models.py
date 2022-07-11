from django.db import models


class Post(models.Model):
    message = models.TextField()
    create_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)