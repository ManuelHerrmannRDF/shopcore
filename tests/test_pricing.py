from shopcore.pricing import calculate_total


def test_calculate_total():

    items = [
        {"price": 10, "quantity": 2},
        {"price": 5, "quantity": 3},
    ]

    result = calculate_total(items)

    assert result == 35
