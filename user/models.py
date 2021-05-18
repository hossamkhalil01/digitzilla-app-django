from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)

from django.db import models


# user object creation manager


class UserManager(BaseUserManager):

    # Normal user creation
    def create_user(self, email, name, password, is_active=True, is_staff=False, is_admin=False, is_superuser=False):

        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not name:
            raise ValueError("Users must have a name")

        user_obj = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        # set user password
        user_obj.set_password(password)

        # set user permssions
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_superuser = is_superuser
        
        # set user to be active
        user_obj.is_active = is_active

        user_obj.save()

        return user_obj

    # Superuser creation
    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError("Admin must have an email address")
        if not password:
            raise ValueError("Admin must have a password")

        superuser = self.create_user(
            email=email,
            name=name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True,
        )
        return superuser

# user model


class User (AbstractBaseUser, PermissionsMixin):

    # Essentials
    email = models.EmailField(
        max_length=255, verbose_name='email', unique=True)
    is_admin = models.BooleanField(default=False, verbose_name='Admin')
    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_active = models.BooleanField(default=False, verbose_name='Active')
    last_login = models.DateTimeField(
        blank=True, null=True, verbose_name='Last Login')
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name='Joining Date')

    # Extensions
    name = models.CharField(max_length=40, verbose_name='name')

    # make email the default
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    # define the required fields
    REQUIRED_FIELDS = ['name']

    # objects creation
    objects = UserManager()

    # when printing the user object display it's name
    def __str__(self):
        return str(self.name)
