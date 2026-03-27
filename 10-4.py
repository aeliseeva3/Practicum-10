def make_payment(P):
    """
    Function that accepts payment.
    :param P: payment by credit card
    :return: None
    """
    try:
        payment = float(P)
        
        if payment < 20:
            print("Повторить попытку")
            return
        
        if payment > 1000:
            print("Повторить попытку")
            return
        
        print("Успех")
        
    except (ValueError, TypeError):
        print("Повторить попытку")


if __name__ == "__main__":
    make_payment(10)

