from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status

from users.models import User
from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, UserListSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsOwnerOrReadOnly()]


class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        email = self.request.query_params.get("email")
        queryset = get_user_model().objects.all()

        if email:
            queryset = queryset.filter(email__icontains=email)
        return queryset


class FollowUserView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = get_object_or_404(User, pk=pk)
        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself"}, status=400)
        request.user.following.add(user_to_follow)
        return Response({"status": "following"})


class UnfollowUserView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({"status": "unfollowed"}, status=status.HTTP_200_OK)


class ListFollowingsView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following = user.following.all()
        serializer = UserSerializer(following, many=True)
        return Response(serializer.data)


class ListFollowersView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.followers.all()
