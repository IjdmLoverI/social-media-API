import pathlib
import uuid

from django.db import models
from django.utils.text import slugify

from users.models import User


def post_image_path(instance: "Post", filename: str) -> pathlib.Path:
    owner_email = instance.owner.email
    filename = f"{slugify(owner_email)}-{uuid.uuid4()}" + pathlib.Path(filename).suffix
    return pathlib.Path("upload/post_img/") / pathlib.Path(filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to=post_image_path)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
