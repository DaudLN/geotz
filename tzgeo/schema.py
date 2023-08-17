import strawberry
from geodata.schema import GeoQuery, GeoMutation
from geodata.auth import AuthQuery, AuthMutation


@strawberry.type
class BaseQuery(GeoQuery, AuthQuery):
    ...


@strawberry.type
class BaseMutation(GeoMutation, AuthMutation):
    ...


schema = strawberry.Schema(query=BaseQuery, mutation=BaseMutation)
