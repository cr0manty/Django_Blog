# Generated by Django 2.2.4 on 2019-09-06 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]