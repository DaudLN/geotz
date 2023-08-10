import graphene


class RegionInputs(graphene.InputObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=False)
