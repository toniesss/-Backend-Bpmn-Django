from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
  
  ADMIN = 1
  STAFF = 2
  User = 3

  ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Manager'),
        (User, 'Employee')
    )
    
  class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

  # Roles created here
  uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=50, blank=True)
  role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
  date_joined = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=True)
  is_deleted = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=timezone.now)
  modified_date = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = CustomUserManager()

  def __str__(self):
        return self.username