# -*- coding: utf-8 -*-
"""
somelist[start:end]
切割列表时，即便start或end索引越界也不会出问题，利用这一特性，我们可以限定序列的最大长度

first_twenty_items= a[:20]
last_twenty_items=a[-20:]
访问列表中的单个元素时，下标不能越界

注意如果使用复变量作为start索引来切割列表，在极个别情况下会出现奇怪的结果
当n为0时，表达式somelist[-0:]会成为原列表的一份拷贝

如果对赋值操作右侧的列表使用切片，而又没有指定起止索引都留空，就会产生一份原列表的拷贝
b=a[:]
assert b == a and b is not a

如果对赋值操作左侧的列表使用切片，而又没有指定起止索引，那么系统会把右侧的新值复制一份，并用这份拷贝来替换左侧列表的全部内容，而不会重新分配新的列表
b=a
a[:] = [193,43,534]
assert a is b
print(a)
"""
