from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length = 30)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    