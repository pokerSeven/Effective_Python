# -*- coding: utf-8 -*-
"""
python2中实现以关键字来指定参数
重要！！
"""
def safe_division_d(number,divisor,**kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow',False)
    ignore_zero_div = kwargs.pop('ignore_zero_divison',False)
    if kwargs:
        raise TypeError('Unexpected **kwargs:%r' % kwargs)
