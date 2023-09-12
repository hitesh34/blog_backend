from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TextBlockViewSet, ImageBlockViewSet, MapBlockViewSet, BlogPostViewSet, ContentBlockViewSet, DataTableBlockViewSet, UserBlockViewSet, CommentViewSet, LatestPostIdView, BlogPostDetailView, CommentApprovalView, CommentRejectionView  


router = DefaultRouter()
router.register(r'text-blocks', TextBlockViewSet)
router.register(r'image-blocks', ImageBlockViewSet)
router.register(r'map-blocks', MapBlockViewSet)
router.register(r'blog-posts', BlogPostViewSet)
router.register(r'content-blocks', ContentBlockViewSet)
router.register(r'data-table-blocks', DataTableBlockViewSet) 
router.register(r'user-blocks', UserBlockViewSet)  
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/latest-post-id/', LatestPostIdView.as_view(), name='latest-post-id'),
    path('api/blog-post/<slug:slug>/', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('api/comments/<int:comment_id>/approve/', CommentApprovalView.as_view(), name='comment-approve'),  # New URL for comment approval
    path('api/comments/<int:comment_id>/reject/', CommentRejectionView.as_view(), name='comment-reject'),  # New URL for comment rejection
]
