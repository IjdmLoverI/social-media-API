import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social_media_API.settings")
django.setup()

from post.models import Post
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_post_list_view_authentication():
    client = APIClient()
    url = reverse('post:post-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_post_list_view_with_email_filter():
    user = User.objects.create_user(email='user@example.com', password='password')
    Post.objects.create(owner=user, title='Test Title', body='Sample Post')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post:post-list')
    response = client.get(url, {'email': 'user@example.com'})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_post_list_view_email_case_insensitivity():
    user = User.objects.create_user(email='user@Example.com', password='password')
    # Again, ensure the correct field names are used
    Post.objects.create(owner=user, title='Test Title', body='Sample Post')
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse('post:post-list')
    response = client.get(url, {'email': 'user@example.com'})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


