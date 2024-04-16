"""
Serializers for recipe app
"""
from rest_framework import serializers
from core.models import (
    Recipe,
    Tag,
    Ingredient,
)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for ingredient"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe"""
    tag = TagSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'price', 'link', 'tag',
            'ingredients',
            ]
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe):
        """Get or create tags for recipe"""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tag.add(tag_obj)

    def _get_or_create_ingredients(self, ingredients, recipe):
        """Get or create ingredients for recipe"""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(
                user=auth_user,
                **ingredient,
            )
            recipe.ingredients.add(ingredient_obj)

    def create(self, validated_data):
        """Create a new recipe"""
        tags = validated_data.pop('tag', [])
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredients(ingredients, recipe)
        return recipe

    def update(self, instance, validated_data):
        """Update a recipe"""
        tags = validated_data.pop('tag', None)
        ingredients = validated_data.pop('ingredients', None)
        if tags is not None:
            instance.tag.clear()
            self._get_or_create_tags(tags, instance)

        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredients(ingredients, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail"""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
