from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.body}" posted by {self.author}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-date_published']


class Like(models.Model):
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             default=None)
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             default=None)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.post}" liked by {self.user}'

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['-time']
