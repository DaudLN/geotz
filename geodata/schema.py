import strawberry
from strawberry.types import Info
from .types import RegionInputType, RegionType
from .models import Region
from typing import List


@strawberry.type
class Query:
    @strawberry.field
    def get_all_regions(self, info: Info) -> List[RegionType]:
        return Region.objects.all()

    @strawberry.field
    def get_region(self, id: strawberry.ID, info: Info) -> RegionType:
        return Region.objects.get(pk=id)

    @strawberry.field
    def me(self, info: Info) -> str:
        return info.context.request.user


@strawberry.type
class Mutation:
    @strawberry.field
    def create_region(self, input: RegionInputType, info: Info) -> RegionType:
        name = input.name
        post_code = input.post_code
        return Region.objects.create(name=name, post_code=post_code)


schema = strawberry.Schema(query=Query, mutation=Mutation)
