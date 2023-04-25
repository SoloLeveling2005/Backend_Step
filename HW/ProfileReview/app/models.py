from django.db import models
from django.forms import ModelForm

# Create your models here.


class Profile(models.Model):
    """
    Модель профиля.
    """
    username = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def estimations(self):
        return Reviews.objects.filter(profile=self)


class Reviews(models.Model):
    """
    Модель профиля.
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_profile')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_user')
    estimation = models.SmallIntegerField()


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'description']
