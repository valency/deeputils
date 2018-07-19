import random
import string
from datetime import datetime
import sys
from django.utils.termcolors import colorize


def log(msg, color="green"):
    """
    Log with colored timestamp
    :param msg: message
    :param color: color, default: green
    :return: none
    """
    print(colorize("[" + format_datetime(datetime.now()) + "]", fg=color), msg)


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()


def digits(n):
    """
    Count the digits of a given float number
    :param n: the float number
    :return: number of digits
    """
    return len(str(n).split('.')[-1])


def random_chars(n):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))


def random_letters(n):
    return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(n))


def random_numbers(n):
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(n))


def dict_search(d, k, v):
    """
    Search dictionary array by key and value
    :param d: dictionary array
    :param k: key
    :param v: value
    :return: the index of the first dictionary in the array with the specific key / value
    """
    for i in range(0, len(d)):
        if d[i][k] == v:
            return i
    return None


def tuple_search(t, i, v):
    """
    Search tuple array by index and value
    :param t: tuple array
    :param i: index of the value in each tuple
    :param v: value
    :return: the first tuple in the array with the specific index / value
    """
    for e in t:
        if e[i] == v:
            return e
    return None


def string_insert(str1, str2, i):
    """
    Insert a string in the middle of another string
    :param str1: the original string
    :param str2: the string to be inserted
    :param i: the index of the insertion position
    :return: the resulting string
    """
    return str1[:i] + str2 + str1[i:]


def format_datetime(t=datetime.now()):
    """
    Format a datetime object into yyyy-MM-dd hh:mm:ss
    :param t: datetime object, default: now
    :return: the formatted string
    """
    return t.strftime('%Y-%m-%d %H:%M:%S')


def format_date(t=datetime.now()):
    """
    Format a datetime object into yyyy-MM-dd
    :param t: datetime object, default: now
    :return: the formatted string
    """
    return t.strftime('%Y-%m-%d')


def format_time(t=datetime.now()):
    """
    Format a datetime object into hh:mm:ss
    :param t: datetime object, default: now
    :return: the formatted string
    """
    return t.strftime('%H:%M:%S')


if __name__ == "__main__":
    log(digits(3.1415926))
    log(chars(3))
    log(dict_search([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], 'a', 1))
    log(tuple_search([('a', 1), ('b', 2), ('a', 3), ('b', 4)], 1, 1))
    log(string_insert('apple', ' is strugg', 3))
    log(format_datetime())
    log(format_date())
    log(format_time())
