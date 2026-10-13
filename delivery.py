"""Расчёт стоимости доставки заказа."""

STANDARD_PRICE = 300
REDUCED_PRICE = 150
FREE_PRICE = 0
EXPRESS_SURCHARGE = 250

REDUCED_THRESHOLD = 1000
FREE_THRESHOLD = 5000


def calculate_delivery(subtotal, express=False):
    """Вернуть стоимость доставки в рублях (без стоимости товаров).

    subtotal -- целая неотрицательная сумма товаров в рублях;
    express  -- True для экспресс-доставки, False для обычной.
    """
    # bool является подклассом int, поэтому исключаем его явно
    if isinstance(subtotal, bool) or not isinstance(subtotal, int):
        raise TypeError("subtotal должен быть целым числом")
    if not isinstance(express, bool):
        raise TypeError("express должен быть логическим значением")
    if subtotal < 0:
        raise ValueError("subtotal не может быть отрицательным")

    if subtotal < REDUCED_THRESHOLD:
        cost = STANDARD_PRICE
    elif subtotal <= FREE_THRESHOLD:
        cost = REDUCED_PRICE
    else:
        cost = FREE_PRICE

    if express:
        cost += EXPRESS_SURCHARGE
    return cost
