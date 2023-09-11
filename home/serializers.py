from rest_framework import serializers
from .models import BlogPost, TextBlock, ImageBlock, MapBlock, ContentBlock, DataTableBlock, UserBlock, Comment, CommentValidation

class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = '__all__'

class ImageBlockSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return obj.image.url

    class Meta:
        model = ImageBlock
        fields = '__all__'
        
class MapBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapBlock
        fields = '__all__'

class DataTableBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTableBlock
        fields = '__all__'


class UserBlockSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    def get_avatar_url(self, obj):
        return obj.avatar.url

    class Meta:
        model = UserBlock
        fields = '__all__'        


class ContentBlockSerializer(serializers.ModelSerializer):
    actual_content = serializers.SerializerMethodField()

    def get_actual_content(self, obj):
        content_type = obj.content_type
        object_id = obj.object_id
        
        # Retrieve the actual model based on the content type
        model_class = content_type.model_class()

        # Fetch the content from the corresponding table using the object_id
        content_instance = model_class.objects.get(pk=object_id)

        # Determine the correct serializer based on the instance type
        if isinstance(content_instance, TextBlock):
            return TextBlockSerializer(content_instance).data
        elif isinstance(content_instance, ImageBlock):
            return ImageBlockSerializer(content_instance).data
        elif isinstance(content_instance, MapBlock):
            return MapBlockSerializer(content_instance).data
        elif isinstance(content_instance, DataTableBlock):  # Add this part
            return DataTableBlockSerializer(content_instance).data
        elif isinstance(content_instance, UserBlock):  # Add this part for UserBlock
            return UserBlockSerializer(content_instance).data
        elif isinstance(content_instance, Comment):  # Add this part for Comment
            return CommentSerializer(content_instance).data
        return None 


    class Meta:
        model = ContentBlock
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'


class CommentValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentValidation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    validation = CommentValidationSerializer(read_only=True)


# class BlogPostSerializer(serializers.ModelSerializer):
#    class Meta:
#         model = BlogPost
#         fields = '__all__'

# class ContentBlockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContentBlock
#         fields = '__all__'

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['content_type'] = {
#             'app_label': instance.content_type.app_label,
#             'model': instance.content_type.model
#         }
#         return representation
