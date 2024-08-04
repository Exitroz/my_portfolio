from django.contrib import admin
from .models import BlogPost, Comment, Tag
# Register your models here.



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(BlogPost)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
