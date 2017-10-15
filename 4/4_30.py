# -*- coding: utf-8 -*-
"""
Python内置的@property修饰器，使开发者可以把类设计得较为轻巧，从而令调用者能够轻松地访问该类的实例属性
此外，@property还可以把简单的数值属性迁移为实时计算的属性，这种用法也是比较常见的
下面时用Python对象实现带有配额的漏桶（漏桶算法时一种具备传输，调度和统计等用途的算法，它把容器比作底部有漏洞的桶，而把配额比作桶底漏出的水）
下面的代码，别当前剩余的配额以及重置配额的周期，放在了Bucket类里面
"""
from datetime import datetime, timedelta


class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.quota = 0

	def __repr__(self):
		return 'Bucket(quota=%d)' % self.quota

	# 漏桶算法若要正常运作，就必须保证：无论向桶中加多少水，都必须在进入下一个周期时将其清空


def fill(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		bucket.quota = 0
		bucket.reset_time = now
	bucket.quota += amount


def deduct(bucket, amount):
	now = datetime.now()
	if now - bucket.reset_time > bucket.period_delta:
		return False
	if bucket.quota - amount < 0:
		return False
	bucket.quota -= amount
	return True


bucket = Bucket(60)
fill(bucket, 100)
print (bucket)

"""
上面这种实现方式的缺点是：以后无法得知漏桶的初始配额。配额会在每个周期内持续流失，如果降到0，那么deduct就终会返回False
此时，依赖deduct的那些炒作，就会受到阻塞，但是，我们却无法判断出：这究竟是由于Bucket里面所剩的配额不足，还是由于Bucket刚开始的时候就没有配额
为了解决这一问题，我们在类中使用max_quot来记录本周期的初始配额，并且用quota_consumed来记录本周期内所消耗的配额
"""


class Bucket(object):
	def __init__(self, period):
		self.period_delta = timedelta(seconds=period)
		self.reset_time = datetime.now()
		self.max_quota = 0
		self.quota_consumed = 0

	def __repr__(self):
		return 'Bucket(max_quota=%d, quota_consumed=%d)' % (self.max_quota, self.quota_consumed)

	@property
	def quota(self):
		return self.max_quota - self.quota_consumed

	@quota.setter
	def quota(self, amount):
		delta = self.max_quota - amount
		if amount == 0:
			self.quota_consumed = 0
			self.max_quota = 0
		elif delta < 0:
			assert self.quota_consumed == 0
			self.max_quota = amount
		else:
			assert self.max_quota >= self.quota_consumed
			self.quota_consumed += delta
