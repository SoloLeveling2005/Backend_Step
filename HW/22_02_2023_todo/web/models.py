from django.db import models


# Create your models here.


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
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    # todo user_id


class Comment(models.Model):
    text = models.CharField(max_length=100)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    # todo user_id
