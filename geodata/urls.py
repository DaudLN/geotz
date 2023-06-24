from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("regions", views.RegionViewSet, basename="regions")
# router.register("districts", views.DistrictViewSet, basename="districts")
# router.register("wards", views.WardViewSet, basename="wards")

region_router = routers.NestedDefaultRouter(router, "regions", lookup="region")
region_router.register("districts", views.DistrictViewSet, basename="region-districts")

district_router = routers.NestedDefaultRouter(
    region_router, "districts", lookup="district"
)
district_router.register("wards", views.WardViewSet, basename="district-wards")

urlpatterns = [
    *router.urls,
    *region_router.urls,
    *district_router.urls,
]
