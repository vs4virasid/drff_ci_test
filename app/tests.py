from django.test import TestCase
from .models import Item


class ItemModelTest(TestCase):
    def test_item_creation(self):
        item = Item.objects.create(name="Test", description="CI/CD Test")
        self.assertEqual(item.name, "Test")
