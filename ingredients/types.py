import graphene

from graphene_django.types import DjangoObjectType
from .models import Category, Ingredient
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        # ordering can be: string, tuple or list
        pagination = LimitOffsetGraphqlPagination(default_limit=2, ordering="-name")
        
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
         # ordering can be: string, tuple or list
        pagination = LimitOffsetGraphqlPagination(
            default_limit=2, ordering="-name")
        