# -*- coding: utf-8 -*-
"""
尽量用异常来表示特殊情况，而不要返回None
"""

"""
错误的做法
"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


"""
正确的做法
"""


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print ('Invalid inputs')
else:
    print ('Result is %.1f' % result)
