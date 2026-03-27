def convert_datetime(datetime_str):
    """
    Converts date and time from "MM/DD/YYYY HR:MIN:SEC" format
    to "DD.MM.YY HR:MIN:SEC" format with 12-hour clock.
    :param datetime_str: String with date and time in "MM/DD/YYYY HR:MIN:SEC" format
    :return: None
    """
    datetime_str = datetime_str.strip()

    if not datetime_str:
        print("Ошибка: Пустая строка")
        return

    try:
        date_part, time_part = datetime_str.split()
    except ValueError:
        print("Ошибка: Неверный формат.")
        return

    try:
        month, day, year = date_part.split('/')
    except ValueError:
        print("Ошибка: Неверный формат даты.")
        return

    try:
        hour, minute, second = time_part.split(':')
    except ValueError:
        print("Ошибка: Неверный формат времени.")
        return

    try:
        month_num = int(month)
        day_num = int(day)
        year_num = int(year)
        hour_num = int(hour)
        minute_num = int(minute)
        second_num = int(second)
    except ValueError:
        print("Ошибка: Все значения должны быть числами")
        return

    if month_num < 1 or month_num > 12:
        print("Ошибка: Неверный номер месяца.")
        return

    days_in_month = [31, 29 if is_leap_year(year_num) else 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    if day_num < 1 or day_num > days_in_month[month_num - 1]:
        print(f"Ошибка: Неверный день для месяца.")
        return

    if year_num < 1 or year_num > 9999:
        print("Ошибка: Неверный год.")
        return

    if hour_num < 0 or hour_num > 23:
        print("Ошибка: Неверный час.")
        return

    if minute_num < 0 or minute_num > 59:
        print("Ошибка: Неверная минута.")
        return

    if second_num < 0 or second_num > 59:
        print("Ошибка: Неверная секунда.")
        return

    year_short = year_num % 100

    if hour_num == 0:
        hour_12 = 12
        period = "AM"
    elif hour_num < 12:
        hour_12 = hour_num
        period = "AM"
    elif hour_num == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour_num - 12
        period = "PM"

    formatted_date = f"{day_num:02d}.{month_num:02d}.{year_short:02d}"
    formatted_time = f"{hour_12}:{minute_num:02d}:{second_num:02d} {period}"

    result = f"{formatted_date} {formatted_time}"
    print(result)


def is_leap_year(year):
    """
    Checks if a year is a leap year.
    :param year: Year to check
    :return: True if the year is a leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    convert_datetime("04/12/1990 13:12:12")

