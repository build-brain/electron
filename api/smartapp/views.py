from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.smartapp.serializers import *


class SubstationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer
    search_fields = "code", "max_power"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(house__user=self.request.user).distinct()


class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filterset_fields = "substation", "user"
    search_fields = "name", "address"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(user=self.request.user)


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_fields = "house", "type"
    search_fields = "name",

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(house__user=self.request.user)


class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filterset_fields = "type", "room", "state"
    search_fields = "name",

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(room__house__user=self.request.user)


class RoomTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    search_fields = "name",


class DeviceTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    search_fields = "name",
