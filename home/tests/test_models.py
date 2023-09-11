from django.test import TestCase
from home.models import BlogPost, TextBlock, ImageBlock, MapBlock, DataTableBlock, UserBlock, Comment

class BlogPostTestCase(TestCase):
    def test_blogpost_creation(self):
        post = BlogPost.objects.create(title="Test Post", slug="test-post")
        retrieved_post = BlogPost.objects.get(slug="test-post")
        self.assertEqual(retrieved_post.title, "Test Post")

class TextBlockTestCase(TestCase):
    def test_textblock_creation(self):
        text_block = TextBlock.objects.create(content="Test Content")
        self.assertEqual(text_block.content, "Test Content")

class ImageBlockTestCase(TestCase):
    def test_imageblock_creation(self):
        image_block = ImageBlock.objects.create(caption="Test Caption")
        self.assertEqual(image_block.caption, "Test Caption")

class MapBlockTestCase(TestCase):
    def test_mapblock_creation(self):
        map_block = MapBlock.objects.create(latitude=40.7128, longitude=-74.0060)
        self.assertEqual(map_block.latitude, 40.7128)
        self.assertEqual(map_block.longitude, -74.0060)

class DataTableBlockTestCase(TestCase):
    def test_datatableblock_creation(self):
        data_table_block = DataTableBlock.objects.create(table_data={"header": ["A", "B"], "data": [["1", "2"], ["3", "4"]]})
        self.assertEqual(data_table_block.table_data, {"header": ["A", "B"], "data": [["1", "2"], ["3", "4"]]})

class UserBlockTestCase(TestCase):
    def test_userblock_creation(self):
        user_block = UserBlock.objects.create(name="Test User", email="test@example.com")
        self.assertEqual(user_block.name, "Test User")
        self.assertEqual(user_block.email, "test@example.com")

class CommentTestCase(TestCase):
    def test_comment_creation(self):
        post = BlogPost.objects.create(title="Test Post", slug="test-post")
        comment = Comment.objects.create(author="Test Author", content="Test Comment", post=post)
        self.assertEqual(comment.author, "Test Author")
        self.assertEqual(comment.content, "Test Comment")
