from django.contrib import admin
from .models import BlogPost, TextBlock, ImageBlock, MapBlock, ContentBlock, DataTableBlock, UserBlock, Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'is_approved', 'created_at', 'post')
    list_filter = ('is_approved',)
    actions = ['approve_comments', 'reject_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    def reject_comments(self, request, queryset):
        queryset.delete()

admin.site.register(Comment, CommentAdmin)

admin.site.register(TextBlock)
admin.site.register(ImageBlock)
admin.site.register(MapBlock)
admin.site.register(BlogPost)
admin.site.register(ContentBlock)
admin.site.register(DataTableBlock)
admin.site.register(UserBlock)
