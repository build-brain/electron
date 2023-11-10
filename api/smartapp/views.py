from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.smartapp.serializers import *
from smartapp.models import *


class HomeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(user=self.request.user)


class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(home__user=self.request.user)


class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(room__home__user=self.request.user)


class RoomTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class DeviceTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
