from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from post.models import Post
from post.serializers import PostSerializer, PostCreateSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(user=self.request.user)
