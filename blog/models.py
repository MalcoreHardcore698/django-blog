from django.db import models

class Post(models.Model):
    class Meta:
        ordering = ['title']
        
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
