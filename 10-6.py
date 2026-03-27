def truncate_message(message):
    """
    Function truncates a message to 160 characters if it exceeds the limit.
    :param message: The message to be truncated
    :return: The original message if its length is less than 160 characters,
             otherwise the first 160 characters of the message
    """
    return message if len(message) < 160 else message[:160]


if __name__ == "__main__":
    test_message = "ffffff"
    print(truncate_message(test_message))

