from django.contrib import admin
from .models import ContactUs,Post,PostCategory,Comment

# Register your models here.

admin.site.register(ContactUs)  
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

