from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.paginator import Paginator


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    deleted_at = models.BooleanField(default=False)

    @classmethod
    def create_user(cls, username: str, password: str):
        user = cls.objects.create(username=username, password=make_password(password))
        return user.id

    def get_user_posts(self):
        if not self.deleted_at:
            return Post.objects.filter(user=self)
        else:
            return {'message': 'user ban'}

    def delete_user(self):
        self.deleted_at = True

    def update_user(self, username: str = None, password: str = None):
        self.username = self.username if username is None else username
        self.password = self.password if password is None else password

    @classmethod
    def users(cls, count: int = 5, page: int = 1):
        users = cls.objects.all()
        users = Paginator(users, count).page(page)
        return users


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    gender = models.BooleanField(default=True)
    age = models.IntegerField(default=18)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    title = models.CharField(max_length=100)
    description = models.TextField()

    @classmethod
    def create_post(cls, user_id: int, title: str, description: str):
        user = User.objects.get(id=user_id)
        cls.objects.create(user=user, title=title, description=description)

    def delete_post(self):
        self.delete()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    text = models.CharField(max_length=150)

    @classmethod
    def create_comment(cls, user_id: int, post_id: str, text: str):
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        cls.objects.create(user=user, text=text, post=post)

    def delete_comment(self):
        self.delete()
