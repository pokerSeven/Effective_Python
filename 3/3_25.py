# -*- coding: utf-8 -*-
""""
用super初始化父类
初始化父类的传统方式，是在子类里用子类实例直接调用父类的__init__方法
"""
class MyBaseClass(object):
	def __init__(self,value):
		self.value = value

class MyChildClass(MyBaseClass):
	def __init__(self):
		MyBaseClass.__init__(self,5)

"""
如果子类受到了多重继承的影响，那么直接调用__init__方法，可能会产生无法预知的行为(调用父类的__init__顺序不同)
"""
