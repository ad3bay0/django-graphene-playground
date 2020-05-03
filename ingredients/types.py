import graphene

from grahene_django.types import DjangoObjectType
from .models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient