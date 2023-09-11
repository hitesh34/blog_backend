from django.test import TestCase, Client
from django.urls import reverse
from home.models import BlogPost, TextBlock, ImageBlock, MapBlock, ContentBlock, DataTableBlock, UserBlock, Comment
from home.views import BlogPostDetailView

class BlogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = BlogPost.objects.create(title="Test Post", slug="test-post")

    def test_blogpost_detail_view(self):
        response = self.client.get(reverse('blog-post-detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_text_block_list_view(self):
        response = self.client.get(reverse('textblock-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_image_block_list_view(self):
        response = self.client.get(reverse('imageblock-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_map_block_list_view(self):
        response = self.client.get(reverse('mapblock-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_blogpost_list_view(self):
        response = self.client.get(reverse('blogpost-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_content_block_list_view(self):
        response = self.client.get(reverse('contentblock-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_datatable_block_list_view(self):
        response = self.client.get(reverse('datatableblock-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_user_block_list_view(self):
        response = self.client.get(reverse('userblock-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_comment_list_view(self):
        response = self.client.get(reverse('comment-list'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_latest_post_id_view(self):
        response = self.client.get(reverse('latest-post-id'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

BlogPostDetailView.lookup_field = 'slug'
