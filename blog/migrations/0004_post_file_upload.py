# Generated by Django 4.2.11 on 2024-04-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_head_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_upload',
            field=models.ImageField(blank=True, upload_to='blog/files/%Y/%m/%d/'),
        ),
    ]