# -*- coding: utf-8 -*-
"""
用None和文档字符串来描述具有动态默认值的参数
下面的函数每次得到的时间戳一样
"""
from datetime import datetime
from time import sleep
def log(message,when = datetime.now()):
    print ('%s: %s' % (when,message))

log('Hi there!')
sleep(0.1)
log('Hi again!')

"""
修改后
"""
def log1(message, when=None):
    """Log a message with a timestamp


    :param message:
    :param when: datetime of when the message occurred
                Defaults to the present time
    :return:
    """
    when = datetime.now() if when is None else when
    print ('%s: %s' % (when, message))

"""
如果参数的实际默认值时可变类型，那就一定要使用None作为形式上的默认值
"""

