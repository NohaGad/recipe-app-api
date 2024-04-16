"""
Test for ingredient API
"""
from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core.models import Ingredient
from recipe.serializers import IngredientSerializer

INGREDIENT_URL = reverse('recipe:ingredient-list')


def detail_url(ingredient_id):
    """Return ingredient detail ID"""
    return reverse('recipe:ingredient-detail', args=[ingredient_id])


def create_user(email='user@example.com', password='test123'):
    """Create and return a new user"""
    return get_user_model().objects.create_user(email=email, password=password)


class PublicIngredientApiTests(TestCase):
    """Test unauthenticated ingredient API access"""

    def setUp(self):
        self.client = APIClient()

    def test_retrive_ingredients_unauthorized(self):
        """Test authentication is required for retrieving ingredients"""
        res = self.client.get(INGREDIENT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateIngredientApiTests(TestCase):
    """
    Tests for authenticates ingredient API access
    """

    def setUp(self):
        self.client = APIClient()
        self.user = create_user()
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredient(self):
        """Test retrieving a list of in gredient is successful"""
        Ingredient.objects.create(user=self.user, name='Cabbage')
        Ingredient.objects.create(user=self.user, name='Cabbage')

        res = self.client.get(INGREDIENT_URL)

        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_ingredients_limited_to_user(self):
        """Test that ingredients for the authenticated user are returned"""
        user2 = create_user(email='user2@example.com', password='user123')
        Ingredient.objects.create(user=user2, name='Cabbage')
        ingredient = Ingredient.objects.create(user=self.user, name='Tumeric')

        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
        self.assertEqual(res.data[0]['id'], ingredient.id)

    def test_update_ingredient(self):
        """Test updating an ingredient"""
        ingredient = Ingredient.objects.create(user=self.user, name='Cabbage')

        payload = {'name': 'Kale'}
        url = detail_url(ingredient.id)

        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        ingredient.refresh_from_db()
        self.assertEqual(ingredient.name, payload['name'])

    def test_delete_ingredient(self):
        """Test deleting an ingredient"""
        ingredient = Ingredient.objects.create(user=self.user, name='Cabbage')
        url = detail_url(ingredient.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        ingredient = Ingredient.objects.filter(user=self.user)
        self.assertFalse(ingredient.exists())
