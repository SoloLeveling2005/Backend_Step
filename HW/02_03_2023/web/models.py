from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    likes = models.BigIntegerField(default=0)

    # todo user_id
    def get_likes(self):
        return Like.objects.filter(post_id=self)

    def get_comments(self):
        return Comment.objects.filter(post_id=self)


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
