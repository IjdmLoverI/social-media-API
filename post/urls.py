from django.urls import path

from post.views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="create-post"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="update-post"),
]

app_name = "post"
