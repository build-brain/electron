from django.db import models
from smartapp.choices import DEVICE_STATE


class House(models.Model):
    name = models.CharField(verbose_name="Name", max_length=15)
    address = models.CharField(verbose_name="Address", max_length=30)
    latitude = models.DecimalField(verbose_name="Latitude", max_digits=10, decimal_places=8, default=0)
    longitude = models.DecimalField(verbose_name="Longitude", max_digits=11, decimal_places=8, default=0)
    user = models.ForeignKey(verbose_name="User", to='management.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"


class Room(models.Model):
    name = models.CharField(verbose_name="Name", max_length=15)
    house = models.ForeignKey(verbose_name="House", to='House', on_delete=models.CASCADE)
    type = models.ForeignKey(verbose_name="Room type", to='RoomType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class RoomType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=15)
    # type = models.ForeignKey('Root', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image", upload_to="./room-type-photos")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Room type"
        verbose_name_plural = "Room types"


class Device(models.Model):
    name = models.CharField(verbose_name="Name", max_length=15)
    state = models.CharField(verbose_name="State", max_length=10, choices=DEVICE_STATE, default="")
    room = models.ForeignKey(verbose_name="Room", to='Room', on_delete=models.CASCADE)
    type = models.ForeignKey(verbose_name="Device Type", to='DeviceType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"


class DeviceType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=15)
    # type int
    icon = models.FileField(verbose_name="Icon", upload_to="./device-icons")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Device Type"
        verbose_name_plural = "Device types"
