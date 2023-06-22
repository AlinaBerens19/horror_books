from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password

class MyAccountManager(BaseUserManager):
    def create_user(self, phone, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone
        )
        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='', null=True)
    surname = models.CharField(max_length=50, default='', null=True)
    email = models.EmailField(max_length=50, default='', unique=True)
    phone = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='media/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'email']

    objects = MyAccountManager()


    def full_name(self):
        return self.name + ' ' + self.surname
    
    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['created']

