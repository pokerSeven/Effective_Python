# -*- coding: utf-8 -*-
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print (numbers)


"""
下面的函数，会出现作用域bug
"""
def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found

#python2中的解决办法
def sort_priority(numbers,group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0,x)
        return 1,x
    numbers.sort(key=helper)
    return found[0]
