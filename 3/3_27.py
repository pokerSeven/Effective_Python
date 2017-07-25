# -*- coding: utf-8 -*-
"""
多用public属性，少用private属性
以两个下划线开头的属性，是private字段，本类的方法可以直接访问它们
在类的外面访问private字段会引发异常
子类无法访问父类的private字段
实现原理：子类之所以无法访问父类的私有属性，只不过是因为变换后的属性名与待访问的属性名不相符


"""
class MyObject(object):
	def __init__(self):
		self.public_field = 5
		self.__private_field = 10
	def get_private_field(self):
		return self.__private_field

foo = MyObject()
assert foo.public_field == 5
assert foo.get_private_field() == 10