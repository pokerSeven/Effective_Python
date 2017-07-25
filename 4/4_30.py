# -*- coding: utf-8 -*-
"""
Python内置的@property修饰器，使开发者可以把类设计得较为轻巧，从而令调用者能够轻松地访问该类的实例属性
此外，@property还可以把简单的数值属性迁移为实时计算的属性，这种用法也是比较常见的
下面时用Python对象实现带有配额的漏桶（漏桶算法时一种具备传输，调度和统计等用途的算法，它把容器比作底部有漏洞的桶，而把配额比作桶底漏出的水）
下面的代码，别当前剩余的配额以及重置配额的周期，放在了Bucket类里面
"""
from datetime import datetime,timedelta

class Bucket(object):
	def __init__(self, period):
		self.period_deta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return 'Bucket(quota=%d)' % self.quota

