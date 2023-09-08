from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost, TextBlock, ImageBlock, MapBlock, DataTableBlock, UserBlock, Comment

class BlogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = BlogPost.objects.create(title="Test Post", slug="test-post")
from django.test import TestCase
from .models import BlogPost  # Import your BlogPost model

class BlogPostTestCase(TestCase):
    def test_blogpost_creation(self):
        # Create the BlogPost instance in the database
        post = BlogPost.objects.create(title="Test Post", slug="test-post")

        # Retrieve the BlogPost instance from the database using the slug
        retrieved_post = BlogPost.objects.get(slug="test-post")

        # Make assertions based on the retrieved BlogPost instance
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
