# -*- coding: utf-8 -*-


class Resistor(object):
	def __init__(self, ohms):
		self.ohms = ohms
		self.voltage = 0
		self.current = 0


class VoltageResistance(Resistor):
	def __init__(self, ohms):
		super(VoltageResistance, self).__init__(ohms)
		self._voltage = 0

	@property
	def voltage(self):
		return self._voltage

	@voltage.setter
	def voltage(self, voltage):
		self._voltage = voltage
		self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print("Before: %5r amps" % r2.current)
r2.voltage = 10
print ('Afer: %5r amps' % r2.current)

"""
为属性指定setter方法时，也可以在方法里面做类型验证及数值验证
!!!下面的类在给构造器传入无效数值，同样会引发异常
"""


class BoundedResistance(Resistor):
	def __init__(self, ohms):
		super(BoundedResistance, self).__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if ohms <= 0:
			raise ValueError('%f ohms must be > 0' % ohms)
		self._ohms = ohms


"""
可以使用@property来防止父类的属性遭到修改
"""


class FixedResistance(Resistor):
	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if hasattr(self, '_ohms'):
			raise AttributeError("Can't set attribute")
		self._ohms = ohms
