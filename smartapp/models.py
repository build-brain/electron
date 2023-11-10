from django.db import models
from smartapp.choices import DEVICE_STATE


class Home(models.Model):
    name = models.CharField(verbose_name="Название", max_length=15)
    address = models.CharField(verbose_name="Адрес", max_length=30)
    latitude = models.DecimalField(verbose_name="Ширина", max_digits=10, decimal_places=8, default=0)
    longitude = models.DecimalField(verbose_name="Долгота", max_digits=11, decimal_places=8, default=0)
    user = models.ManyToManyField(verbose_name="Пользователь", to='management.User')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"


class Room(models.Model):
    name = models.CharField(verbose_name="Название", max_length=15)
    home = models.ForeignKey(verbose_name="Дом", to='Home', on_delete=models.CASCADE)
    type = models.ForeignKey(verbose_name="Тип комнаты", to='RoomType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class RoomType(models.Model):
    name = models.CharField(verbose_name="Название", max_length=15)
    # type = models.ForeignKey('Root', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Изображение", upload_to="./room-type-photos")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип комнаты"
        verbose_name_plural = "Типы комнат"


class Device(models.Model):
    name = models.CharField(verbose_name="Название", max_length=15)
    state = models.CharField(verbose_name="Состояние", max_length=10, choices=DEVICE_STATE, default="")
    room = models.ForeignKey(verbose_name="Комната", to='Room', on_delete=models.CASCADE)
    type = models.ForeignKey(verbose_name="Тип устройства", to='DeviceType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"


class DeviceType(models.Model):
    name = models.CharField(verbose_name="Название", max_length=15)
    # type int
    icon = models.FileField(verbose_name="Иконка", upload_to="./device-icons")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип устройства"
        verbose_name_plural = "Типы устройств"
