# -*- coding: utf-8 -*-
"""
只在使用Mix-in组件制作工具类时进行多重继承
mix-in类是一种小型的类，它只定义了其他类可能需要提供的一套附加方法，而不定义自己的实例属性，此外，它也不要求使用者调用自己的__init__构造器

例如，要把内存中的Python对象转换为字典形式，以便将其序列化，
"""


class ToDictMixin(object):
	def to_dict(self):
		return self._traverse_dict(self.__dict__)

	def _traverse_dict(self, instance_dict):
		output = {}
		for key, value in instance_dict.items():
			output[key] = self._traverse(key, value)
		return output

	def _traverse(self, key, value):
		if isinstance(value, ToDictMixin):
			return value.to_dict()
		elif isinstance(value, dict):
			return self._traverse_dict(value)
		elif isinstance(value, list):
			return [self._traverse(key, i) for i in value]
		elif hasattr(value, '__dict__'):
			return self._traverse_dict(value.__dict__)
		else:
			return value


class BinaryTree(ToDictMixin):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)),
				  right=BinaryTree(13, left=BinaryTree(11)))
print (tree.to_dict())


class BinaryTreeWithParent(BinaryTree):
	def __init__(self, value, left=None, right=None, parent=None):
		super(BinaryTreeWithParent, self).__init__(value, left=left, right=right)
		self.parent = parent
	def _traverse(self, key, value):
		if (isinstance(value,BinaryTreeWithParent)) and key=='parent':
			return value.value
		else:
			return super(BinaryTree,self)._traverse(key,value)

root = BinaryTreeWithParent(10)
root.left = BinaryTreeWithParent(7,parent=root)
root.left.right = BinaryTreeWithParent(9,parent=root.left)
print (root.to_dict())