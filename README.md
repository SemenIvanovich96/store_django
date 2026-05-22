Важно: для проверки логирования.
Чтобы создать товар, потребуется создать категорию.
Например:
Python manage.py shell
from store.models import Category
Category.objects.create(name="Одежда").
Затем в самом приложение пробуем создать товар.
Проверяем логирование в терминале worker'a.

