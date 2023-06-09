# Generated by Django 4.2 on 2023-05-11 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_replyreaction_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='created_add',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='updated_ad',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='reaction',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='posts.tweet'),
        ),
    ]
