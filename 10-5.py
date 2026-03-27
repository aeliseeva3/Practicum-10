def calculate_card_value():
    """
    Function asks the user for the card cost.
    :return: Total value of the card with bonus, or None if an error occurs
    """
    try:
        card_cost = int(input())
    except ValueError:
        print("Ошибка: Пожалуйста, введите число.")
        return None

    if card_cost == 5 or card_cost == 10:
        bonus = 0
    elif card_cost == 25:
        bonus = 3
    elif card_cost == 50:
        bonus = 8
    elif card_cost == 100:
        bonus = 20
    else:
        print("Ошибка: Недопустимое значение.")
        return None

    total_value = card_cost + bonus

    return total_value


if __name__ == "__main__":
    print(calculate_card_value())

