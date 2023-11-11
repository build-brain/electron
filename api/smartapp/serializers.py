from rest_framework import serializers

from smartapp.models import *


class SubstationSerializer(serializers.ModelSerializer):
    load = serializers.ReadOnlyField(source="get_load")

    class Meta:
        model = Substation
        fields = "__all__"


class HouseSerializer(serializers.ModelSerializer):
    substation_name = serializers.ReadOnlyField(source="substation.__str__")
    substation_load = serializers.ReadOnlyField(source="substation.get_load")

    class Meta:
        model = House
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    house_name = serializers.ReadOnlyField(source="house.__str__")
    type_name = serializers.ReadOnlyField(source="type.__str__")

    class Meta:
        model = Room
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    room_name = serializers.ReadOnlyField(source="room.__str__")
    type_name = serializers.ReadOnlyField(source="type.__str__")

    class Meta:
        model = Device
        fields = "__all__"


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = "__all__"
        