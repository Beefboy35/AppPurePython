
def verify_date(date: str): # функция для верификации даты
    date = date.split("-")
    if len(date) == 3:
        year, month, day = date
    else:
        raise ValueError("Incorrect date")
    if int(year) < 2024:
        raise ValueError({"Error": "You can't change your past)) Year must be >= 2024"})
    elif int(month) > 12 or  int(month) < 1:
        raise ValueError({"Error": "month must be in the range[1-12]"})
    elif int(day) > 31 or int(day) < 1:
        raise ValueError({"Error": "day must be in the range[1-31]"})
    elif (int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12) and int(day) > 31:
        raise ValueError({"Error": "There are 31 days in January, March, May, July, August, October, December"})
    elif (int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11) and int(day) > 30:
        raise ValueError({"Error": "There are 30 days in April, June, September, November"})
    elif int(year) not in [2024, 2028, 2032, 2036, 2040] and int(month) == 2 and int(day) > 28  or int(year) in [2024, 2028, 2032, 2036, 2040] and int(month) == 2 and int(day) > 29:
        raise ValueError({"Error": "There are 28 days in February and 29 days once in 4 years"})
    return "-".join(date)