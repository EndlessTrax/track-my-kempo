from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Technique(models.Model):
    title = models.CharField(max_length=50)
    notes = models.TextField()
    # Consider changing default DateTime
    date_practiced = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, default='Uncategorized')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.title} was practiced last on: {self.date_practiced}'
