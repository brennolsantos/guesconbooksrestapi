from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
import re
from django.core import validators

# Create your models here.

# Model User


class User(AbstractBaseUser, PermissionsMixin):
    """
    User is the customizes User model 
    It implements ZIP code, complete name, country 
    and Phone
    """

    username = models.CharField('Username', max_length=30, unique=True, validators=[
                                validators.RegexValidator(re.compile('^[\w.@+-]'))])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Name', max_length=200, blank=True)
    zip_code = models.CharField('Zip', max_length=15, blank=True)
    country = models.CharField('Country', max_length=40, blank=True)
    phone_number = models.CharField('Phone', max_length=20, blank=True)
    is_active = models.BooleanField('Is Active?', blank=True, default=True)
    is_staff = models.BooleanField('Is Staff?', blank=True, default=False)
    date_joined = models.DateTimeField('Join Date', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
