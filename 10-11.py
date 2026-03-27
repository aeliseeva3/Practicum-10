def is_prime(number):
    """
    Logical function that determines whether a number is prime.
    :param number: The number to check
    :return: True if the number is prime, False otherwis
    """
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    numbers = 3
    while numbers * numbers <= number:
        if number % numbers == 0:
            return False
        numbers += 2

    return True


def print_primes_up_to_n():
    """
    Asks the user for a number N and prints all prime numbers from 1 to N.
    :return: None
    """
    try:
        n = int(input())

        if n < 1:
            print("Ошибка: N должно быть натуральным числом.")
            return

        if is_prime(n):
            print(f"\nЧисло {n} является простым")
        else:
            print(f"\nЧисло {n} не является простым")

        print(f"\nПростые числа от 1 до {n}:")

        primes_found = []
        for number in range(1, n + 1):
            if is_prime(number):
                primes_found.append(number)

        if primes_found:
            print(" ".join(map(str, primes_found)))
        else:
            print("Простые числа не найдены")

    except ValueError:
        print("Ошибка.Введите целое число")


if __name__ == "__main__":
    print_primes_up_to_n()

