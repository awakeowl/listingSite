import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of username.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Defines a custom user with a role and reason for app usage"""
    objects = CustomUserManager()

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        EDITOR = "EDITOR", 'Editor'
        VIEWER = "VIEWER", 'Viewer'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(
        max_length=20, choices=Roles.choices, default=Roles.VIEWER)
    email = models.EmailField(_('email address'), unique=True)

    @classmethod
    def get_user_by_email(cls, email):
        return cls.objects.get(email=email)

    def __str__(self):
        return f"{self.id}"

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
