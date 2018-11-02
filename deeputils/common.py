import random
import string
import sys
import time
from datetime import datetime
from heapq import heappush, heappop

from django.utils.termcolors import colorize


def log(msg, color="green"):
    """
    Log with colored timestamp
    :param msg: message
    :param color: color, default: green
    :return: none
    """
    print(colorize("[" + format_datetime(datetime.now()) + "]", fg=color), msg)


def digits(n):
    """
    Count the digits of a given float number
    :param n: the float number
    :return: number of digits
    """
    return len(str(n).split('.')[-1])


def random_chars(n):
    """
    Generate a random string from a-zA-Z0-9
    :param n: length of the string
    :return: the random string
    """
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(n))


def random_letters(n):
    """
    Generate a random string from a-zA-Z
    :param n: length of the string
    :return: the random string
    """
    return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(n))


def random_numbers(n):
    """
    Generate a random string from 0-9
    :param n: length of the string
    :return: the random string
    """
    return ''.join(random.SystemRandom().choice(string.digits) for _ in range(n))


def dict_search(d, k, v):
    """
    Search dictionary list by key and value
    :param d: dictionary list
    :param k: key
    :param v: value
    :return: the index of the first dictionary in the array with the specific key / value
    """
    for i in range(len(d)):
        if d[i][k] == v:
            return i
    return None


def dict_merge(a, b, k):
    """
    Merge two dictionary lists
    :param a: original list
    :param b: alternative list, element will replace the one in original list with same key
    :param k: key
    :return: the merged list
    """
    c = a.copy()
    for j in range(len(b)):
        flag = False
        for i in range(len(c)):
            if c[i][k] == b[j][k]:
                c[i] = b[j].copy()
                flag = True
        if not flag:
            c.append(b[j].copy())
    return c


def dict_sort(d, k):
    """
    Sort a dictionary list by key
    :param d: dictionary list
    :param k: key
    :return: sorted dictionary list
    """
    return sorted(d.copy(), key=lambda i: i[k])


def dict_top(d, k, n, reverse=False):
    """
    Return top n of a dictionary list sorted by key
    :param d: dictionary list
    :param k: key
    :param n: top n
    :param reverse: whether the value should be reversed
    :return: top n of the sorted dictionary list
    """
    h = list()
    for i in range(len(d)):
        heappush(h, (-d[i][k] if reverse else d[i][k], i))
    r = list()
    while len(r) < n and len(h) > 0:
        _, i = heappop(h)
        r.append(d[i].copy())
    return r


def dict_flatten(d):
    """
    Replace the values of a dict with certain type to other values
    :param d: the dictionary
    :return: flattened dictionary
    """
    if type(d) != dict:
        return d
    else:
        dd = dict()
        for key, value in d.items():
            if type(value) == dict:
                for k, v in value.items():
                    dd[key + '_' + k] = dict_flatten(v)
            else:
                dd[key] = value
        return dd


def dict_format_type(d, source, formatter, include_list=True):
    """
    Replace the values of a dict with certain type to other values
    :param d: the dictionary
    :param source: the source type, e.g., int
    :param formatter: the formatter method, e.g., return the string format of an int
    :param include_list: whether list should be formatted, otherwise list will be considered as source type
    :return: formatted dictionary
    """
    if type(d) != dict:
        if type(d) == source:
            return formatter(d)
        else:
            return d
    else:
        dd = dict()
        for key, value in d.items():
            if include_list and type(value) == list:
                dd[key] = [dict_format_type(i, source, formatter) for i in value]
            elif type(value) == dict:
                dd[key] = dict_format_type(value, source, formatter)
            elif type(value) == source:
                dd[key] = formatter(value)
            else:
                dd[key] = value
        return dd


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


def format_datetime(t=None):
    """
    Format a datetime object into yyyy-MM-dd hh:mm:ss
    :param t: datetime object, default: now
    :return: the formatted string
    """
    return (datetime.now() if t is None else t).strftime('%Y-%m-%d %H:%M:%S')


def format_date(t=None):
    """
    Format a datetime object into yyyy-MM-dd
    :param t: datetime object, default: now
    :return: the formatted string
    """
    return (datetime.now() if t is None else t).strftime('%Y-%m-%d')


def format_time(t=None):
    """
    Format a datetime object into hh:mm:ss
    :param t: datetime object, default: now
    :return: the formatted string
    """
    return (datetime.now() if t is None else t).strftime('%H:%M:%S')


def progress(count, total, prefix='', suffix='', length=60):
    """
    Show a progress bar
    :param count: current progress
    :param total: total progress
    :param prefix: prefix shown before the progress bar
    :param suffix: suffix shown after the progress bar
    :param length: length of the progress bar, default: 60
    :return: none
    """
    bar_len = length
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('%s[%s] %s%s%s\r' % (prefix, bar, percents, '%', ' ' + suffix))
    sys.stdout.flush()


def test():
    def modify(u):
        return str(u + 1)

    log(digits(3.1415926))
    log(random_chars(3))
    log(random_letters(3))
    log(random_numbers(3))
    log(dict_search([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], 'a', 1))
    log(dict_merge([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], [{'a': 1, 'b': 3}, {'a': 2, 'b': 4}], 'a'))
    log(dict_sort([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 1, 'b': 3}, {'a': 2, 'b': 4}], 'a'))
    log(dict_top([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, {'a': 1, 'b': 3}, {'a': 2, 'b': 4}], 'a', 2, reverse=True))
    log(dict_flatten({'a': 1, 'b': 'b', 'c': [1, 2], 'd': {'a': 1, 'b': 2}, 'e': [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]}))
    log(dict_format_type({'a': 1, 'b': 'b', 'c': [1, 2], 'd': {'a': 1, 'b': 2}, 'e': [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]}, int, modify))
    log(tuple_search([('a', 1), ('b', 2), ('a', 3), ('b', 4)], 1, 1))
    log(string_insert('apple', ' strugg', 3))
    log(format_datetime(datetime.fromtimestamp(datetime.now().timestamp() + 3600 * 24)))
    log(format_date())
    log(format_time())
    for x in range(100):
        progress(x, 100)
        time.sleep(0.02)


if __name__ == "__main__":
    test()
