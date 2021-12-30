from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from .managers import CustomUserManager
from django.core.mail import send_mail


class MyAccountManager(BaseUserManager):
    """
        This is a manager for Account class
    """

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an Emaill address")
        if not username:
            raise ValueError("Users must have an Username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        """
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        """

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """
      Custom user class inheriting AbstractBaseUser class
    """

    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    title = models.CharField(max_length=30, null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.ImageField(verbose_name=_("Photo"), upload_to='profile/', default='profile/default-user-avatar.png')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    #REQUIRED_FIELDS = []


    objects = MyAccountManager()

    class Meta:
        ordering = ['date_joined']
        # verbose_name = _('user')
        # verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)