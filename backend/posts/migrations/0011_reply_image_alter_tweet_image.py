# Generated by Django 4.2 on 2023-05-23 05:18

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_reply_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='image',
            field=models.ImageField(default='No image', upload_to=posts.models.reply_image_store),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(default='No image', upload_to=posts.models.tweet_image_store),
            preserve_default=False,
        ),
    ]