# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/10/11 16:27'

def trace(func):
	def wrapper(*args,**kwargs):
		result = func(*args,**kwargs)
		print '%s(%r, %r) -> %r' % (func.__name__, args, kwargs, result)
		return result
	return wrapper

@trace
def fibonacci(n):
	"""Retrun the n-th Fibonacci number"""
	if n in (0,1):
		return n
	return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(3)
