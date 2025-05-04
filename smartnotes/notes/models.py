from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

