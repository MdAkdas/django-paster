from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=20,
        unique=True,
        help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    status = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars', default='avatars/guest.png')
    about = models.TextField(blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __unicode__(self):
        return self.email
