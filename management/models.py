from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from random import randint
import re

from .services.reset_password import send_otp


class UserManager(BaseUserManager):
    """ User Manager To create superuser. """

    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Users must have a phone_number")
        user = self.model(phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(phone_number=phone_number, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom User model. """

    phone_number = models.CharField(verbose_name="Номер телефона", unique=True, max_length=20, null=False, blank=False)

    first_name = models.CharField(verbose_name="Имя", max_length=20)
    last_name = models.CharField(verbose_name="Фамилия", max_length=20, null=True, blank=True)

    is_active = models.BooleanField(verbose_name="Активный", default=True)
    is_staff = models.BooleanField(verbose_name="Сотрудник", default=False)
    registered_at = models.DateTimeField(verbose_name="Дата регистрации", auto_now_add=True)

    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    class Meta:
        verbose_name = "Ползователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        self.phone_number = re.sub(r'[()\s-]', '', self.phone_number)
        super().save(*args, **kwargs)
    
    def reset_password(self):
        otp = randint(1000, 9999)
        self.set_password(str(otp))
        self.save()
        return send_otp(self.phone_number, otp)


class Panel(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    power = models.IntegerField(verbose_name="Power", default=0, help_text="In kW")
    annual_productivity = models.FloatField(verbose_name="Annual productivity", default=0, help_text="In mW")
    guarantee_period = models.IntegerField(verbose_name="Guarantee period", default=0, help_text="In year")
    price = models.DecimalField(verbose_name="Price", default=0, max_digits=12, decimal_places=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Panel"
        verbose_name_plural = "Panels"

