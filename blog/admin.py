from django.contrib import admin
from .models import Post, Comment

class PostModelAdmin(admin.ModelAdmin):
    '''Adds fields to the post portion in the admin view'''
    list_display = ["title", "published_date", "created_date"]
    list_display_links = ["published_date"]
    list_editable = ["title"]
    list_filter = ["published_date"]
    search_fields = ["title", "text"]
    class Meta:
        model = Post


class CommentModelAdmin(admin.ModelAdmin):
    '''Adds fields to the comment portion in the admin view'''
    list_display = ["post", "created_date"]
    list_display_links = ["created_date"]
    search_fields = ["text"]
    class Meta:
        model = Comment

# make these available in the Admin panel
admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
