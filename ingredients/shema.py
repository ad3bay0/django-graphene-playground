import graphene

from .types import CategoryType, IngredientType
from .models import Category, Ingredient

class Query(object):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all();
    
    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()