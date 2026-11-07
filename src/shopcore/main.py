from shopcore.pricing import calculate_total


def test_calculate_total():
    print("Testing calculate_total function ...")
    cart = [
        {"price": 10, "quantity": 2},
        {"price": 5, "quantity": 3},
    ]

    total = calculate_total(cart)
    print(f"Total price for the cart: {total}")


def run():
    print("Starting ShopCore ...")
    test_calculate_total()


if __name__ == "__main__":
    run()
