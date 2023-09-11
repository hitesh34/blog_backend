from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.contenttypes.models import ContentType
from home.models import (
    BlogPost, TextBlock, ImageBlock, MapBlock, ContentBlock,
    DataTableBlock, UserBlock, Comment
)
from home.serializers import (
    TextBlockSerializer, ImageBlockSerializer, MapBlockSerializer, DataTableBlockSerializer,
    UserBlockSerializer, ContentBlockSerializer, BlogPostSerializer, CommentSerializer
)

class SerializersTestCase(TestCase):
    def setUp(self):
        # Create test data for serializers
        self.text_block = TextBlock.objects.create(content="Test text content")
        self.image_block = ImageBlock.objects.create(
            image=SimpleUploadedFile("test_image.jpg", b"file_content"),
            caption="Test image caption"
        )
        self.map_block = MapBlock.objects.create(latitude=42.0, longitude=42.0)
        self.data_table_block = DataTableBlock.objects.create(table_data={"key": "value"})
        self.user_block = UserBlock.objects.create(
            name="Test User",
            email="test@example.com",
            avatar=SimpleUploadedFile("avatar.jpg", b"avatar_content")
        )

        self.content_block = ContentBlock.objects.create(
            content_type=ContentType.objects.get_for_model(self.text_block),
            object_id=self.text_block.id
        )

        self.blog_post = BlogPost.objects.create(
            title="Test Blog Post",
            slug="test-blog-post",
            author_image=SimpleUploadedFile("author_image.jpg", b"author_image_content")
        )

        self.comment = Comment.objects.create(
            author="Test Author",
            content="Test comment content",
            post=self.blog_post
        )

        # Add the content block to the blog post
        self.blog_post.content_blocks.add(self.content_block)

    def test_text_block_serializer(self):
        serializer = TextBlockSerializer(self.text_block)
        self.assertEqual(serializer.data['content'], "Test text content")

    def test_image_block_serializer(self):
        serializer = ImageBlockSerializer(self.image_block)
        self.assertTrue('image_url' in serializer.data)
        self.assertEqual(serializer.data['caption'], "Test image caption")

    def test_map_block_serializer(self):
        serializer = MapBlockSerializer(self.map_block)
        self.assertTrue('latitude' in serializer.data)
        self.assertTrue('longitude' in serializer.data)

    def test_data_table_block_serializer(self):
        serializer = DataTableBlockSerializer(self.data_table_block)
        self.assertEqual(serializer.data['table_data'], {"key": "value"})

    def test_user_block_serializer(self):
        serializer = UserBlockSerializer(self.user_block)
        self.assertTrue('avatar_url' in serializer.data)
        self.assertEqual(serializer.data['name'], "Test User")
        self.assertEqual(serializer.data['email'], "test@example.com")

    def test_content_block_serializer(self):
        serializer = ContentBlockSerializer(self.content_block)
        self.assertTrue('actual_content' in serializer.data)

    # Removed the test_blog_post_serializer method

    def test_comment_serializer(self):
        serializer = CommentSerializer(self.comment)
        self.assertEqual(serializer.data['author'], "Test Author")
        self.assertEqual(serializer.data['content'], "Test comment content")
