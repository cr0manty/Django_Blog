# Generated by Django 2.2.4 on 2019-08-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
