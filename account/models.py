from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(user_model,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
