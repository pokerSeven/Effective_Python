# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/15 9:46'

from  weakref import WeakKeyDictionary
class Homework(object):
	def __init__(self):
		self._grade = 0

	@property
	def grade(self):
		return self._grade

	@grade.setter
	def grade(self, value):
		if not (0 <= value <= 100):
			raise ValueError('Grade must be between 0 and 100')
		self._grade = value


class Exam(object):
	def __init__(self):
		self._writing_grade = 0
		self._math_grade = 0

	@staticmethod
	def _check_grade(value):
		if not (0 <= value <= 100):
			raise ValueError('Grade must be between 0 and 100')


class Grade(object):
	def __init__(self):
		self._values = WeakKeyDictionary()

	def __get__(self,instance,value):
		if instance is None: return self
		print "instance",instance
		return self._values.get(instance,0)

	def __set__(self,instance,value):
		self._values[instance] = value


class Exam(object):
	 math_grade = Grade()
	 writing_grade = Grade()
	 science_grade = Grade()

exam = Exam()
exam1 = Exam()
exam.writing_grade = 40
print exam.writing_grade
exam1.writing_grade = 99
print exam1.writing_grade

