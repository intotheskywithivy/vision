from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['post_user', 'post_time', 'post_title', 'post_body']
    list_display = ('post_user', 'post_time', 'post_title', 'post_body')
    search_fields = ['post_user', 'post_time', 'post_title', 'post_body']

admin.site.register(Post, PostAdmin)
