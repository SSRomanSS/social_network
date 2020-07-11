from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    user = models.ForeignKey(get_user_model(),
                             related_name='likes',
                             on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return f'"{self.body}" posted by {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-date_published']

    @property
    def likes_sum(self):
        return self.likes.count()
