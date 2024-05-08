from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import CreateUserView, ManageUserView, UserListView, UserDetailView, FollowUserView, UnfollowUserView, \
    ListFollowingsView, ListFollowersView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create_user"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("list/", UserListView.as_view(), name="user_list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path('<int:pk>/follow/', FollowUserView.as_view(), name='follow_user'),
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('followings/', ListFollowingsView.as_view(), name='list_followings'),
    path('users/followers/', ListFollowersView.as_view(), name='list_followers'),
]

app_name = "users"
