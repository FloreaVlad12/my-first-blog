# Generated by Django 2.2.12 on 2020-06-02 12:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_picture_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='likes',
            field=models.ManyToManyField(blank=True, default=0, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
