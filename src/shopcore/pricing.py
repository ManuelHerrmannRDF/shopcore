def calculate_total(items: list) -> float:
    total = 0

    for item in items:
        price = item.get("price")
        quantity = item.get("quantity")

        if price < 0 or quantity < 0:
            raise ValueError("Preis und Menge dürfen nicht negativ sein")

        total += price * quantity

    return total
