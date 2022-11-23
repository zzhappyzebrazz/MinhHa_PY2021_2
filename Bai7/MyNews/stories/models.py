from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return self.name
    
class Story(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150, unique=True)
    author = models.CharField(max_length=250)
    url = models.URLField(null=True)
    summary = models.TextField(null=True, blank=True)
    content = models.TextField()
    public_day = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='stories/images', default='stories/images/logo.jpg')
    viewed = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name