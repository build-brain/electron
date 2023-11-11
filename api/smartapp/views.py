from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from api.smartapp.serializers import *


class SubstationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Substation.objects.all()
    serializer_class = SubstationSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = "code", "max_power"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(house__user=self.request.user)


class HouseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = "substation",
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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = "",
    search_fields = "name",
    ordering_fields = "",

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(house__user=self.request.user)


class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = "",
    search_fields = "name",
    ordering_fields = "",

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        
        return queryset.filter(room__house__user=self.request.user)


class RoomTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = "",
    search_fields = "name",
    ordering_fields = "",


class DeviceTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = "",
    search_fields = "name",
    ordering_fields = "",
