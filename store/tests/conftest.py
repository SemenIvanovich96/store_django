import pytest

from store.models import Category, Product


@pytest.fixture
def category_1():
    return Category.objects.create(name="Тестовая категория")


@pytest.fixture
def product_1(category_1):
    return Product.objects.create(
        name="Телефон",
        description="Смартфон с 128 ГБ",
        price=19999.00,
        category=category_1,
        is_published=False,
    )


@pytest.fixture
def product_2(category_1):
    return Product.objects.create(
        name="Ноутбук",
        description="Игровой ноутбук",
        price=79999.00,
        category=category_1,
        is_published=True,
    )
