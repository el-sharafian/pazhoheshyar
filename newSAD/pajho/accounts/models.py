from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, personal_id, password=None, **extra_fields):
        if not personal_id:
            raise ValueError('The Personal ID must be set')
        user = self.model(personal_id=personal_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, personal_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(personal_id, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    personal_id = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    degree = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'personal_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'email', 'degree', 'student_id']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
