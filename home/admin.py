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

@admin.register(BlogPost)  # Register BlogPost with the admin site
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'publication_date', 'last_modified', 'date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Comment, CommentAdmin)
admin.site.register(TextBlock)
admin.site.register(ImageBlock)
admin.site.register(MapBlock)
admin.site.register(ContentBlock)
admin.site.register(DataTableBlock)
admin.site.register(UserBlock)
