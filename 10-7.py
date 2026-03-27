def print_common_multiples(A, B, N):
    """
    Function prints all common multiples of numbers A and B that do not exceed N.
    :param A: first number
    :param B: second number
    :param N: does not exceed N number
    :return: None
    """
    found = False

    for number in range(1, N + 1):
        if number % A == 0 and number % B == 0:
            print(number, end=" ")
            found = True

    if not found:
        print(f"Нет общих кратных")


if __name__ == "__main__":
    print_common_multiples(2, 4, 12)

