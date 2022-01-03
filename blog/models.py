from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=150)
    title_tag = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=150, default='uncategorised')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    
    def get_absolute_url(self):
        return reverse('home')
