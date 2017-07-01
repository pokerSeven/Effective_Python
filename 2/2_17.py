# -*- coding: utf-8 -*-
"""
注意，迭代器只能产生一轮结果，在抛出过StopIteration异常的迭代器或生产器上面继续迭代第二轮，是不会有结果的
"""


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


"""
可以使用迭代器制作一份列表
注意：如有大量数据，可能会耗尽内存而崩溃
"""


def normalize_copy(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


"""
通过参数来接受另外一个函数，函数每次调用后，都返回新的迭代器
"""


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


"""
实现迭代器协议的容器类
"""
class ReadVisits(object):
    def __init__(self,data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


