import pytest
from store.models import Product


@pytest.mark.django_db
def test_create_product(product_1, product_2):
    """Проверка создания товаров."""
    assert Product.objects.count() == 2
    assert product_1.name == "Телефон"
    assert product_1.price == 19999.00
    assert product_1.is_published is False
    assert product_2.name == "Ноутбук"
    assert product_2.price == 79999.00
    assert product_2.is_published is True


@pytest.mark.django_db
def test_read_product(product_1, product_2):
    """Проверка чтения товаров."""
    obj_1 = Product.objects.get(pk=product_1.pk)
    obj_2 = Product.objects.get(pk=product_2.pk)
    assert obj_1 == product_1
    assert obj_2 == product_2


@pytest.mark.django_db
def test_update_product(product_1):
    """Проверка обновления товара."""
    product_1.name = "Обновлённый телефон"
    product_1.price = 24999.00
    product_1.is_published = True
    product_1.save()
    obj = Product.objects.get(pk=product_1.pk)
    assert obj.name == "Обновлённый телефон"
    assert obj.price == 24999.00
    assert obj.is_published is True


@pytest.mark.django_db
def test_delete_product(product_1):
    """Проверка удаления товара."""
    pk = product_1.pk
    product_1.delete()
    assert not Product.objects.filter(pk=pk).exists()
