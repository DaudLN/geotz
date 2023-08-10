from rest_framework.viewsets import ModelViewSet

from .models import District, Region, Ward
from .serializers import DistrictSerializer, RegionSerializer, WardSerializer
from rest_framework import permissions


class RegionViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    queryset = Region.objects.prefetch_related("districts").all()
    serializer_class = RegionSerializer

    def get_serializer_context(self):
        return self.kwargs


class DistrictViewSet(ModelViewSet):
    serializer_class = DistrictSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_queryset(self):
        return (
            District.objects.filter(region_id=self.kwargs["region_pk"])
            .prefetch_related("wards")
            .select_related("region")
            .all()
        )

    def get_serializer_context(self):
        return {"region_id": self.kwargs.get("region_pk")}


class WardViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    queryset = Ward.objects.select_related("district", "district__region").all()
    serializer_class = WardSerializer

    def get_queryset(self):
        return Ward.objects.filter(district_id=self.kwargs["district_pk"]).all()

    def get_serializer_context(self):
        return {
            "region_id": self.kwargs.get("region_pk"),
            "district_id": self.kwargs.get("district_pk"),
        }
