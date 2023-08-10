from typing import List
import strawberry
from strawberry import django
from . import models


@django.type(models.Region, name="RegionType", select_related="districts")
class RegionType:
    id: strawberry.ID
    name: str
    slug: str
    post_code: int
    districts: List["DistrictType"]


@django.type(models.District, name="DistrictType")
class DistrictType:
    id: strawberry.ID
    name: str
    slug: str


@django.input(models.Region, name="RegionInputType")
class RegionInputType:
    name: str
    post_code: int
