# -*- coding: utf-8 -*-
"""
以@classmethod形式的多态去通用得构建对象
多态，使得继承体系中的多个类都能以各自所独有的方法来实现某个方法
例如，下面为了实现一套MapReduce流程，我们需要定义公共基类来表示输入的数据。
下面就定义了这样的基类，它的read方法必须由子类来实现：
"""
import os
import threading


class InputData(object):
	def read(self):
		raise NotImplementedError


class PathInputData(InputData):
	def __init__(self, path):
		super(PathInputData, self).__init__()
		self.path = path

	def read(self):
		return open(self.path).read()


class Worker(object):
	def __init__(self, input_data):
		self.input_data = input_data
		self.result = None

	def map(self):
		raise NotImplementedError

	def reduce(self, other):
		raise NotImplementedError


class LineCountWorker(Worker):
	def map(self):
		data = self.input_data.read()
		self.result = data.count('\n')

	def reduce(self, other):
		self.result += other.result


def generate_inputs(data_dir):
	for name in os.listdir(data_dir):
		yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
	workers = []
	for input_data in input_list:
		workers.append(LineCountWorker(input_data))
	return workers


def execute(workers):
	threads = [threading.Thread(target=w.map) for w in workers]
	for thread in threads: thread.start()
	for thread in threads: thread.join()

	first, rest = workers[0], workers[1:]
	for worker in rest:
		first.reduce(worker)
	return first.result


def mapreduce(data_dir):
	inputs = generate_inputs(data_dir)
	wokers = create_workers(inputs)
	return execute(wokers)


result = mapreduce(
	"F:\\pythonproject\\Effective_Python\\2")
print ("There are", result, "lines")

"""
上面的写法有大问题，MapReduce函数不够通用。我们需要使用一种通用的方法来构建对象

下面是使用@classmethod形式的多态。
"""


class GenericInputData(object):
	def read(self):
		raise NotImplementedError

	@classmethod
	def generate_inputs(cls, config):
		raise NotImplementedError


class PathInputData(GenericInputData):
	def read(self):
		return open(self.path).read()

	@classmethod
	def generate_inputs(cls, config):
		data_dir = config['data_dir']
		for name in os.listdir(data_dir):
			yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
	def map(self):
		raise NotImplementedError

	def reduce(self, other):
		raise NotImplementedError

	@classmethod
	def create_workers(cls, input_class, config):
		workers = []
		for input_data in input_class.generate_inputs(config):
			workers.append(cls(input_data))
		return workers
