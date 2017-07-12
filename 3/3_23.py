# -*- coding: utf-8 -*-
"""
很多内置API，允许调用者传入函数，定制其行为。
例如：
    list类型的sort方法接受可选的key参数，用以指定每个索引位置上的值之间应该如何排序
"""
from collections import defaultdict

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print (names)

"""
定制defaultdict类的行为，允许使用者提供一个函数，以后在查询本字典时，如果里面没有待查的键，那就用这个函数为该键创建新值。
"""
def log_missing():
    print ("Key added")
    return 0

current = {
    'green': 12,
    'blue':3
}

increments = [('red',5),
              ('blue',17),
              ('orange',9),]
result = defaultdict(log_missing,current)
print ('Before:',dict(result))
for key,amount in increments:
    result[key] += amount
print ('After:',dict(result))


"""
现在要给defaultdict 传入一个产生默认值的挂钩，并令其统计出该字典一共遇到了多少个缺少的键。
下面使用的是带状态的闭包
注：在python2中没有nonlocal，下面使用列表进行变通
"""
def increment_with_report(current,increments):
    added_count = [0]

    def missing():
        added_count[0] += 1
        return  0
    result = defaultdict(missing,current)
    for key,amount in increments:
        result[key] += amount

    return result, added_count[0]

result,count = increment_with_report(current,increments)
assert count == 2

"""
带状态的闭包函数用作挂钩有一个缺点，就是读起来要比无状态的函数难懂一些。
还可以定义一个小型的类，把需要追踪的状态封装起来
"""
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing,current)

for key, amount in increments:
    result[key] += amount
assert counter.added == 2

"""
使用上述辅助类来改写带状态的闭包，确实要比increment_with_report函数清晰。但是单看这个类，我们依然不太容易理解CountMissing的意图。
CountMissing对象由水来构建？missing方法由谁来调用？该类以后是否需要添加新的公共方法？这些问题，都必须等看过了defaultdict的用法之后
，才能明白。
为了厘清这些问题，我们可以在Python代码中定义名为__call__的特殊方法。
该方法使相关对象能够想函数那样得到调用。此外如果把这样的实例传给内置的callable函数，那么callable函数会返回True
"""
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()

result = defaultdict(counter,current)

for key, amount in increments:
    result[key] += amount
assert counter.added == 2