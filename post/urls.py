from django.urls import path

from post.views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path("posts/", PostListView.as_view(), name="borrowing-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="borrowing-detail"),
    path("posts/create/", PostCreateView.as_view(), name="create-borrowing"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="return-borrowing"),
]

app_name = "post"
