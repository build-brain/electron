from django.db import models
from smartapp.choices import DEVICE_STATE
from utils.helpers import get_substation_load


class Substation(models.Model):
    code = models.CharField(verbose_name="CODE", max_length=10, unique=True)
    latitude = models.DecimalField(verbose_name="Latitude", max_digits=10, decimal_places=8, default=0)
    longitude = models.DecimalField(verbose_name="Longitude", max_digits=11, decimal_places=8, default=0)
    max_power = models.IntegerField(verbose_name="Max Power", help_text="In KW", default=0)

    def __str__(self):
        return self.code

    def get_load(self):
        load = int((get_substation_load(self.code)/self.max_power)*100)  # In percent
        return load

    class Meta:
        verbose_name = "Substation"
        verbose_name_plural = "Substations"


class House(models.Model):
    def default_substation(self):
        print(self.pk)
        substation = Substation.objects.order_by(
            "latitude", "longitude", "house__latitude", "house__longitude").first()
        if substation:
            return substation.pk
        return None

    substation = models.ForeignKey(
        verbose_name="Substation", to="Substation", default=default_substation,
        on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=15)
    address = models.CharField(verbose_name="Address", max_length=30)
    latitude = models.DecimalField(verbose_name="Latitude", max_digits=10, decimal_places=8, default=0)
    longitude = models.DecimalField(verbose_name="Longitude", max_digits=11, decimal_places=8, default=0)
    user = models.ForeignKey(verbose_name="User", related_name="house", to='management.User', on_delete=models.CASCADE)

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
