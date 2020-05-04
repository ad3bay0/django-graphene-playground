import graphene

from ingredients.shema import Query as IngredientQuery

class Query(IngredientQuery, graphene.ObjectType):
    
    pass

schema = graphene.Schema(query=Query)