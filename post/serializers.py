from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "title",
            "owner",
            "body",
            "image",
            "posted_on"
        )
        read_only_fields = ("id", "posted_on")

    def get_owner(self, obj):
        return obj.owner.email


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "image",
            "posted_on"
        )
        read_only_fields = ("id", "posted_on")
