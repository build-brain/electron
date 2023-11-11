from datetime import timedelta, datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
from random import randint
import re

from .services.sender import send_otp, send_reset


class UserManager(BaseUserManager):
    """ User Manager To create superuser. """

    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Users must have a phone number")

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

    phone_number = models.CharField(verbose_name="Phone number", unique=True, max_length=20)

    first_name = models.CharField(verbose_name="Name", max_length=20, null=True, blank=True)
    last_name = models.CharField(verbose_name="Surname", max_length=20, null=True, blank=True)

    otp = models.IntegerField(verbose_name="OTP")
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_try = models.IntegerField(default=settings.MAX_OTP_TRY)
    otp_max_out = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(verbose_name="Active", default=False)
    is_staff = models.BooleanField(verbose_name="Staff", default=False)
    registered_at = models.DateTimeField(verbose_name="Date of registered", auto_now_add=True)

    USERNAME_FIELD = "phone_number"

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        self.phone_number = re.sub(r'[()\s-]', '', self.phone_number)
        super().save(*args, **kwargs)
    
    def reset_password(self):
        password = randint(100000, 999999)
        self.set_password(str(password))
        self.save()
        return send_reset(self.phone_number, password)

    def verify_otp(self, otp):
        if not self.is_active and self.otp == otp and self.otp_expiry and datetime.now() < self.otp_expiry:
            print("active")
            self.is_active = True
            self.otp_expiry = None
            self.max_otp_try = settings.MAX_OTP_TRY
            self.otp_max_out = None
            self.save()
            return True
        
        return False

    def regenerate_otp(self):
        if self.max_otp_try == 0 and datetime.now() < self.otp_max_out:
            return False

        otp = randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes=10)
        max_otp_try = self.max_otp_try - 1

        self.otp = otp
        self.otp_expiry = otp_expiry
        self.max_otp_try = max_otp_try
        if max_otp_try == 0:
            # Set cool downtime
            otp_max_out = datetime.now() + timedelta(hours=1)
            self.otp_max_out = otp_max_out
        elif max_otp_try == -1:
            self.max_otp_try = settings.MAX_OTP_TRY
        else:
            self.otp_max_out = None
            self.max_otp_try = max_otp_try
        self.save()
        send_otp(self.phone_number, otp)
        return True


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

