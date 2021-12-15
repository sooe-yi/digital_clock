import datetime


def show_time():
    time = get_time()
    return time


def get_time():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    time = f"{hour}:{minute}:{second}"
    return time
