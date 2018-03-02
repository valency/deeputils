from datetime import datetime

from django.utils.termcolors import colorize


def log(msg, color="green"):
    print(colorize("[" + format_datetime(datetime.now()) + "]", fg=color), msg)


def dict_search(d, k, v):
    for i in range(0, len(d)):
        if d[i][k] == v:
            return i
    return None


def tuple_search(t, k, v):
    for e in t:
        if e[k] == v:
            return e
    return None


def string_insert(str1, str2, i):
    return str1[:i] + str2 + str1[i:]


def format_datetime(t=datetime.now()):
    return t.strftime('%Y-%m-%d %H:%M:%S')


def format_date(t=datetime.now()):
    return t.strftime('%Y-%m-%d')


def format_time(t=datetime.now()):
    return t.strftime('%H:%M:%S')


if __name__ == "__main__":
    log(format_datetime())
    log(format_date())
    log(format_time())
