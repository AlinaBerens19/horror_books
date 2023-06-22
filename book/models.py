from django.db import models

from account.models import User

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    published_date = models.CharField(max_length=100, blank=True, default='')
    publisher = models.CharField(max_length=100, blank=True, default='')
    updated = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=50, default='English')
    genre = models.CharField(max_length=50, default='Fiction')
    ranking = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE, null=True)
    highlighted = models.TextField(null=True)
    image = models.ImageField(upload_to='media/', null=True)
    category = models.CharField(max_length=100, blank=True, default='New')
    trending = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created']

