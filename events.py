import datetime

def events():
    today = datetime.date.today()

    if datetime.date.weekday(datetime.date.today()) == 4:
        return "happy #friday!"
    elif today == datetime.date(today.year, 10, 31):
        return "happy #halloween!"
    elif today == datetime.date(today.year, 12, 25):
        return "merry #christmas"
    elif today == datetime.date(today.year, 2, 22):
        return "it's my owner's birthday today!"
    elif today == datetime.date(today.year, 1, 1):
        return "happy #newyear"
    else:
        return ""