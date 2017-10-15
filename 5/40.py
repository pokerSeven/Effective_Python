# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/8/6 3:06'

def my_coroutine():
	r = "fd"
	while True:
		received = yield r
		print ('Received:', received)
		r = "rer"
it = my_coroutine()
print next(it)
it.send('First')
it.send('Second')
print next(it)