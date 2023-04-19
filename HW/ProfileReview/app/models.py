from django.db import models
from django.forms import ModelForm

# Create your models here.


class Profile(models.Model):
    """
    Модель профиля.
    """
    username = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def estimation(self):
        return Reviews.objects.get(profile=self)


class Reviews(models.Model):
    """
    Модель профиля.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    estimation = models.SmallIntegerField()


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'description']
