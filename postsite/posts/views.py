from django.shortcuts import render
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer
from core.permissions import AllowGETUnauthenticated

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowGETUnauthenticated]
    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
        return super().create(request, *args, **kwargs)
