# Generated by Django 3.0.8 on 2020-07-11 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['-time'], 'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='like',
            name='object_id',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]