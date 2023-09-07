from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

class BaseStamp(models.Model):
    time_created = models.DateTimeField(default=timezone.now)
    time_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ContentBlock(BaseStamp):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['order']

class TextBlock(BaseStamp):
    content = models.TextField()

    def split_paragraphs(self):
        return self.content.split('\n\n')

class ImageBlock(BaseStamp):
    image = models.ImageField(upload_to='blog_images/')
    caption = models.CharField(max_length=300)

    def image_url(self):
        return self.image.url

class MapBlock(BaseStamp):
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom_level = models.PositiveIntegerField(default=10)

class BlogPost(BaseStamp):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=500, blank=True)  # Allow blank values
    slug = models.SlugField(unique=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    date = models.DateField(default=timezone.now)  # Add default value for date field

    content_blocks = models.ManyToManyField(ContentBlock)

    class Meta:
        ordering = ['-publication_date']

class DataTableBlock(BaseStamp):
    table_data = models.JSONField()

class UserBlock(BaseStamp):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='blog_images/')

    def image_url(self):
        return self.image.url

class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Add this field

    class Meta:
        ordering = ['order', '-created_at']  # Order by 'order' field and then 'created_at'
