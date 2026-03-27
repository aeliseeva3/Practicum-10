def print_numbers(A, B):
    """
    Prints all numbers in the range from A to B that consist only of digits 1, 3, 4, 8, 9.
    :param A: Starting number of the range (integer)
    :param B: Ending number of the range (integer)
    :return: None
    """
    if A > B:
        A, B = B, A

    allowed = "13489"

    for number in range(A, B + 1):
        number_str = str(number)
        valid = True
        for digit in number_str:
            if digit not in allowed:
                valid = False
                break

        if valid:
            print(number, end=" ")


if __name__ == "__main__":
    try:
        a = 5
        b = 10
        print_numbers(a, b)
    except ValueError:
        print("Ошибка. Недопустимое значение")

