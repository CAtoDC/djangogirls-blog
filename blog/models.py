from django.db import models
from django.utils import timezone


class Post(models.Model):
    # database fields
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # returns the blog post name
    def __str__(self):
        return self.title
