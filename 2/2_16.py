# -*- coding: utf-8 -*-
"""
下面的代码是查每个词的首字母
有两个问题
1.代码过于拥挤
2.输入量非常大师，程序可能耗尽内存并崩溃
"""


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


"""
使用生成器
"""


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
