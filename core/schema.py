import graphene

from ingredients.shema import Query as IngredientQuery

class Query(IngredientQuery):
    
    pass

schema = graphene.Schema(query=Query)