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
    email = models.EmailField(max_length=50, default='', unique=True)
    phone = models.CharField(max_length=50, unique=True, default='')
    updated = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, default='')
    profile_picture = models.ImageField(upload_to='media/', null=True, blank=True)
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True, default='')
    country = models.CharField(max_length=30, blank=True, default='')
    city = models.CharField(max_length=30, blank=True, default='')
    name = models.CharField(max_length=50, default='', null=True)
    surname = models.CharField(max_length=50, default='', null=True)
    phone = models.CharField(max_length=50, unique=True)
    zip_code = models.CharField(max_length=30, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    
    def email(self):
        return self.user.email
    
    class Meta:
        ordering = ['created']

