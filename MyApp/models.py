from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('index', args=self.pk )
