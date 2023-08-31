from rest_framework import serializers

from .models import Post
from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['pk', "writer", "content", "created_at", "updated_at"]
        read_only_fields = ["pk"]