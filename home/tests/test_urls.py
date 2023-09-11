from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import (
    TextBlockViewSet, ImageBlockViewSet, MapBlockViewSet, BlogPostViewSet,
    ContentBlockViewSet, DataTableBlockViewSet, UserBlockViewSet, CommentViewSet,
    LatestPostIdView, BlogPostDetailView
)

class TestUrls(SimpleTestCase):
    def test_text_block_list_url_resolves(self):
        url = reverse('textblock-list')
        self.assertEqual(resolve(url).func.cls, TextBlockViewSet)

    def test_image_block_list_url_resolves(self):
        url = reverse('imageblock-list')
        self.assertEqual(resolve(url).func.cls, ImageBlockViewSet)

    def test_map_block_list_url_resolves(self):
        url = reverse('mapblock-list')
        self.assertEqual(resolve(url).func.cls, MapBlockViewSet)

    def test_blog_post_list_url_resolves(self):
        url = reverse('blogpost-list')
        self.assertEqual(resolve(url).func.cls, BlogPostViewSet)

    def test_content_block_list_url_resolves(self):
        url = reverse('contentblock-list')
        self.assertEqual(resolve(url).func.cls, ContentBlockViewSet)

    def test_data_table_block_list_url_resolves(self):
        url = reverse('datatableblock-list')
        self.assertEqual(resolve(url).func.cls, DataTableBlockViewSet)

    def test_user_block_list_url_resolves(self):
        url = reverse('userblock-list')
        self.assertEqual(resolve(url).func.cls, UserBlockViewSet)

    def test_comment_list_url_resolves(self):
        url = reverse('comment-list')
        self.assertEqual(resolve(url).func.cls, CommentViewSet)

    def test_latest_post_id_url_resolves(self):
        url = reverse('latest-post-id')
        self.assertEqual(resolve(url).func.cls, LatestPostIdView)

    def test_blog_post_detail_url_resolves(self):
        url = reverse('blog-post-detail', args=['test-slug'])  # Replace 'test-slug' with an actual slug
        self.assertEqual(resolve(url).func.cls, BlogPostDetailView)
