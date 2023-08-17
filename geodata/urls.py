from django.urls import path
from rest_framework_nested import routers
from strawberry.django.views import GraphQLView
from . import views
from django.views.decorators.csrf import csrf_exempt
from tzgeo.schema import schema

router = routers.DefaultRouter(trailing_slash=False)
router.register("regions", views.RegionViewSet, basename="regions")
router.register("districts", views.DistrictViewSet, basename="districts")
router.register("wards", views.WardViewSet, basename="wards")

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
    path("graphql/", csrf_exempt(GraphQLView.as_view(schema=schema))),
]
