# Generated by Django 5.0.4 on 2024-05-06 12:37

import post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=post.models.post_image_path),
        ),
    ]
