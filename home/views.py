from rest_framework import viewsets
from .models import BlogPost, TextBlock, ImageBlock, MapBlock, ContentBlock, DataTableBlock, UserBlock, Comment 
from .serializers import (
    BlogPostSerializer, TextBlockSerializer,
    ImageBlockSerializer, MapBlockSerializer, ContentBlockSerializer, DataTableBlockSerializer, UserBlockSerializer, CommentSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.db.models import F

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

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


class AllCommentsView(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.annotate(post_title=F('post__title'))
    serializer_class = CommentSerializer


class CommentApprovalView(APIView):
    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

        if comment.is_approved:
            return Response({'message': 'Comment is already approved'})

        comment.is_approved = True
        comment.save()
        return Response({'message': 'Comment approved'})

class CommentRejectionView(APIView):
    def post(self, request, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

        if not comment.is_approved:
            return Response({'message': 'Comment is already rejected'})

        comment.is_approved = False
        comment.save()
        return Response({'message': 'Comment rejected'})