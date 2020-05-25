from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length = 30)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    abstract = RichTextField()
    text = RichTextField()
    category = models.ForeignKey(PostCategory,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.title    

class Comment(models.Model):
    author = models.CharField(max_length=64)
    text = models.CharField(max_length=128)
    is_reviewed = models.BooleanField(default=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return self.text    
