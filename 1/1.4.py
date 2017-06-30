# -*- coding: utf-8 -*-
"""
从url中解码查询字符串
"""
from urlparse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))

"""
查询字符串中的参数
('Red:      ', ['5'])
('Green:    ', [''])
('Opacity:  ', None)
"""
print("Red:      ",my_values.get('red'))
print("Green:    ",my_values.get('green'))
print("Opacity:  ",my_values.get('Opacity'))

def get_first_int(values,key,defaut=0):
    found = values.get(key,[''])
    if found[0]:
        found = int(found[0])
    else:
        found = defaut
    return found
