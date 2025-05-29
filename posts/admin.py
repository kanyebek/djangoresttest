from django.contrib import admin
from posts.models import Post,Comment
# Register your models here.

class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author__username']
    list_filter = ['created_at', 'updated_at']
    list_display = ['title', 'author', 'created_at', 'updated_at']
    inlines = [CommentInLine]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)