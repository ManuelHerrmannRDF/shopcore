def calculate_total(items: list) -> float:
    total = 0

    for item in items:
        total += item.get("price") * item.get("quantity")

    return total
