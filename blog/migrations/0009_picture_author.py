# Generated by Django 2.2.12 on 2020-06-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='author',
            field=models.CharField(default='Vlad', max_length=100),
        ),
    ]