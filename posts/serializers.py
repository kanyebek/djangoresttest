from rest_framework import serializers
from posts.models import Post, Comment
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def validate(self, attrs):
        return super().validate(attrs)
    

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):
        return super().validate(attrs)

