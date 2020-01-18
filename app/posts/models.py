from django.db import models

from members.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    like_user = models.ManyToManyField(
        User, through='PostLike', related_name='like_post_set',
    )
    created = models.DateTimeField(auto_now_add=True)


class PostImage(models.Model):
    image = models.ImageField()
    # post (N) - PostImage (M) 관계가 아닌가?
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostComment(models.Model):
    # post 같은 경우 M:N관계가 아닌가?
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author(1) : PostComment(N-F)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class PostLike(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


