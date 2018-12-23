from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from .managers import UserManager


class User(TimeStampedModel,
           AbstractBaseUser,
           PermissionsMixin):
    email = models.EmailField(_('email'), max_length=255, unique=True)
    name = models.CharField(_('name'), max_length=25)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
