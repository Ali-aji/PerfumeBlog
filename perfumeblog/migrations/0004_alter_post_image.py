# Generated by Django 4.2 on 2023-04-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfumeblog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
