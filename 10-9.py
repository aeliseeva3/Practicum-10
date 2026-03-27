def seconds_since_new_year(datetime_str):
    """
    Calculates the number of seconds elapsed since the beginning of the year (01/01/YYYY 00:00:00).
    :param datetime_str: String with date and time in format "MM/DD/YYYY HR:MIN:SEC"
    :return: Number of seconds since the beginning of the year, or None if an error occurs
    """
    datetime_str = datetime_str.strip()

    if not datetime_str:
        print("Ошибка: Пустая строка")
        return None

    try:
        date_part, time_part = datetime_str.split()
    except ValueError:
        print("Ошибка: Неверный формат.")
        return None

    try:
        month, day, year = date_part.split('/')
    except ValueError:
        print("Ошибка: Неверный формат даты.")
        return None

    try:
        hour, minute, second = time_part.split(':')
    except ValueError:
        print("Ошибка: Неверный формат времени.")
        return None

    try:
        month_num = int(month)
        day_num = int(day)
        year_num = int(year)
        hour_num = int(hour)
        minute_num = int(minute)
        second_num = int(second)
    except ValueError:
        print("Ошибка: Все значения должны быть числами")
        return None

    if not is_valid_date(month_num, day_num, year_num):
        return None

    if not is_valid_time(hour_num, minute_num, second_num):
        return None

    days_passed = calculate_days_since_new_year(month_num, day_num, year_num)

    total_seconds = (days_passed * 24 * 3600) + (hour_num * 3600) + (minute_num * 60) + second_num

    return total_seconds


def is_leap_year(year):
    """
    Checks if a year is a leap year.
    :param year: Year to check
    :return: True if the year is a leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def is_valid_date(month, day, year):
    """
    Checks the validity of a date.
    :param month: Month (1-12)
    :param day: Day
    :param year: Year
    :return: True if the date is valid, False otherwise
    """
    if month < 1 or month > 12:
        print("Ошибка. Неверный месяц.")
        return False

    days_in_month = [31, 29 if is_leap_year(year) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    if day < 1 or day > days_in_month[month - 1]:
        print("Ошибка. Неверный день.")
        return False

    if year < 1 or year > 9999:
        print("Ошибка. Неверный год.")
        return False

    return True


def is_valid_time(hour, minute, second):
    """
    Checks the validity of a time.
    :param hour: Hours (0-23)
    :param minute: Minutes (0-59)
    :param second: Seconds (0-59)
    :return: True if the time is valid, False otherwise
    """
    if hour < 0 or hour > 23:
        print("Ошибка: Неверный час.")
        return False

    if minute < 0 or minute > 59:
        print("Ошибка: Неверная минута.")
        return False

    if second < 0 or second > 59:
        print("Ошибка: Неверная секунда.")
        return False

    return True


def calculate_days_since_new_year(month, day, year):
    """
    Calculates the number of days elapsed since the beginning of the year up to the specified date.
    :param month: Month
    :param day: Day
    :param year: Year
    :return: Number of days since the beginning of the year (0-364 or 0-365)
    """
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[1] = 29

    days_passed = 0
    for number in range(month - 1):
        days_passed += days_in_month[number]

    days_passed += day - 1

    return days_passed


if __name__ == "__main__":
    print(seconds_since_new_year("01/02/2024 00:00:00"))

