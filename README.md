# delivery-ci

**ФИО:** Ларпер Алекс Иванович
**Группа:** 4СПИ

Лабораторная работа: разработка автотестов и их запуск с помощью GitHub Actions.

Модуль `delivery.py` содержит функцию `calculate_delivery(subtotal, express=False)`,
которая рассчитывает стоимость доставки заказа в рублях:

| Сумма товаров  | Обычная | Экспресс |
|----------------|---------|----------|
| 0 – 999        | 300     | 550      |
| 1000 – 4999    | 150     | 400      |
| от 5000        | 0       | 250      |

Отрицательная сумма → `ValueError`, некорректный тип `subtotal`/`express` → `TypeError`.

## Установка зависимостей

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt
```

## Локальный запуск тестов

```bash
python -m pytest -q
```
