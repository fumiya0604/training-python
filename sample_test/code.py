def calc_tax(price, is_exempt):
    """
    税の計算、非課税パターンあり
    """
    if is_exempt:
        return price
    else:
        return price * 1.1


def main():
    price = 1000
    price_with_tax = calc_tax(price, False)
    print("price with tax :", int(price_with_tax))

    price_without_tax = calc_tax(price, True)
    print("price without tax :", price_without_tax)


if __name__ == "__main__":
    main()
