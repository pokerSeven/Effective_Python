# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/8/6 2:57'

import subprocess

proc = subprocess.Popen(['echo','Hello from the child!'], stdout=subprocess.PIPE)
out, err = proc.communicate()
print out.decode('utf-8')
