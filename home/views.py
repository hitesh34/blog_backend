from rest_framework import viewsets
from .models import BlogPost, TextBlock, ImageBlock, MapBlock, ContentBlock, DataTableBlock, UserBlock, Comment 
from .serializers import (
    BlogPostSerializer, TextBlockSerializer,
    ImageBlockSerializer, MapBlockSerializer, ContentBlockSerializer, DataTableBlockSerializer, UserBlockSerializer, CommentSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TextBlockViewSet(viewsets.ModelViewSet):
    queryset = TextBlock.objects.all()
    serializer_class = TextBlockSerializer

class ImageBlockViewSet(viewsets.ModelViewSet):
    queryset = ImageBlock.objects.all()
    serializer_class = ImageBlockSerializer

class MapBlockViewSet(viewsets.ModelViewSet):
    queryset = MapBlock.objects.all()
    serializer_class = MapBlockSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ContentBlockViewSet(viewsets.ModelViewSet):
    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockSerializer

class DataTableBlockViewSet(viewsets.ModelViewSet):
    queryset = DataTableBlock.objects.all()
    serializer_class = DataTableBlockSerializer

class UserBlockViewSet(viewsets.ModelViewSet):
    queryset = UserBlock.objects.all()
    serializer_class = UserBlockSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LatestPostIdView(APIView):
    def get(self, request, *args, **kwargs):
        latest_comment = Comment.objects.last()
        latest_post_id = latest_comment.post.id + 1 if latest_comment else 1
        return Response({'latest_post_id': latest_post_id})

