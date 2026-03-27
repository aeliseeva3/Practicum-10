def calculate_final_price(purchase_amount, discount_card, holiday):
    """
    Function calculates the final cost of the product.
    :param purchase_amount: purchase price
    :param discount_card: availability of a discount card
    :param holiday: public holiday
    :return: final price
    """
    if purchase_amount < 0:
        raise ValueError("Стоимость покупки не может быть отрицательной")
    
    purchase_amount = round(purchase_amount, 2)
    
    total_discount = 0
    
    if purchase_amount > 30000:
        total_discount += 10
    elif purchase_amount > 20000:
        total_discount += 7
    elif purchase_amount > 15000:
        total_discount += 5
    elif purchase_amount > 5000:
        total_discount += 3
    
    if discount_card:
        total_discount += 5
    
    if holiday:
        total_discount += 3
    
    total_discount = min(total_discount, 15)
    
    discount_amount = purchase_amount * total_discount / 100
    
    final_price = purchase_amount - discount_amount
    final_price = round(final_price, 2)
    
    return final_price


if __name__ == "__main__":
    print(calculate_final_price(5000.275, False, False))

