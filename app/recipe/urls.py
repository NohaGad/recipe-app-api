"""
Mapping for recipe APIs
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from recipe import views

router = DefaultRouter()
router.register('recipe', views.RecipeViewSet)
router.register('tag', views.TagViewSet)
router.register('ingredient', views.IngredienViewSet)


app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
