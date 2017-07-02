# -*- coding: utf-8 -*-
"""
用数量可变的位置参数减少视觉杂讯
"""


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

"""
使用可变位置参数会出现两个问题：
1.变长参数在传给函数时，总是要转化成原组。如果用带有*操作符的生成器为参数，来调用这种函数，那么Python就必须先把该生成器完整得迭代一轮，并把生成器所生成的每一个值都放入原组中。这可能会消耗大量内存，并导致程序崩溃。
2.若要给函数添加新的位置参数，就必须修改原来调用该函数的那些旧代码。（通常只能以关键字形式指定的参数来进行扩展）
"""