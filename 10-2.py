def fibonacci(number):
    """
    Function for the Fibonacci sequence. 
    :param number: up to what number should the sequence be
    :return: None
    """
    a, b = 1, 1

    for i in range(number):
        print(a, end=" ")
        a, b = b, a + b

    print()   


if __name__ == "__main__":
    N = 5
    fibonacci(N)

