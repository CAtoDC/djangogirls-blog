from django.contrib import admin
from .models import Post, Comment

# make these available in the Admin panel
admin.site.register(Post)
admin.site.register(Comment)
