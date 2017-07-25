# -*- coding: utf-8 -*-
"""
下面是继承Python内置的list类型，创建的自定义的列表，并统计各元素出现频率的方法
"""


class FrequencyList(list):
	def __init__(self, members):
		super(FrequencyList, self).__init__(members)

	def frequency(self):
		counts = {}
		for item in self:
			counts.setdefault(item, 0)
			counts[item] += 1
		return counts


foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print ('Length is', len(foo))
foo.pop()
print ('after pop', repr(foo))
print ('frequency:', foo.frequency())

"""
假设要编写这么一种对象：它本身不属于list子类，但是用起来却和list一样，也可以通过下标访问其中的元素。
例如，我们要令下面这个表示二叉树节点的类，也能够像list或tuple等序列那样来访问。

"""


class BinaryNode(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


"""
使用下标访问元素时
bar = [1,2,3]
bar[0]
Python 会把访问代码转译为：
bar.__getitem__(0)
于是，我们提供自己的__getitem__方法，令BinaryNode类可以表现得和序列一样。
下面这个方法按深度优先的次序来访问二叉树中的对象
"""


class IndexableNode(BinaryNode):
	def _search(self, count, index):
		# ...
		# Return(found,count)
		pass
	def __getitem__(self, index):
		found,_ = self._search(0,index)
		if not found:
			raise IndexError('Index out of range')
		return found.value
