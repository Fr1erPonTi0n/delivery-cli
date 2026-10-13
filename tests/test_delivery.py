import pytest

from delivery import calculate_delivery


@pytest.mark.parametrize(
    "subtotal, expected",
    [
        (0, 300),
        (500, 300),
        (999, 300),
        (1000, 150),
        (2500, 150),
        (4999, 150),
        (5000, 0),
        (12000, 0),
    ],
)
def test_standard_delivery(subtotal, expected):
    assert calculate_delivery(subtotal) == expected
    assert calculate_delivery(subtotal, express=False) == expected


@pytest.mark.parametrize(
    "subtotal, expected",
    [
        (0, 550),
        (999, 550),
        (1000, 400),
        (4999, 400),
        (5000, 250),
        (12000, 250),
    ],
)
def test_express_delivery(subtotal, expected):
    assert calculate_delivery(subtotal, express=True) == expected


def test_express_is_disabled_by_default():
    assert calculate_delivery(1500) == calculate_delivery(1500, express=False)


def test_result_is_int():
    assert isinstance(calculate_delivery(1000, express=True), int)


@pytest.mark.parametrize("subtotal", [-1, -1000])
def test_negative_subtotal_raises_value_error(subtotal):
    with pytest.raises(ValueError):
        calculate_delivery(subtotal)


@pytest.mark.parametrize("subtotal", ["1000", 1000.0, None, [1000], True, False])
def test_invalid_subtotal_type_raises_type_error(subtotal):
    with pytest.raises(TypeError):
        calculate_delivery(subtotal)


@pytest.mark.parametrize("express", ["yes", 1, 0, None])
def test_invalid_express_type_raises_type_error(express):
    with pytest.raises(TypeError):
        calculate_delivery(1000, express=express)
