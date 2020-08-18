import logging
import numpy as np 


def get_number(data):
	"""Takes array of length which can be divided by 784, 
	reshapes it to 28x28 and predicts number using neural network"""
	if not isinstance(data, list):
		return None
	data = prepare(data)
	


def prepare(arr):
	if (len(data) % 784) != 0:
		return None
	data = np.array(data, dtype='float32')
	data /= 255
	data = data.reshape((int(len(data)**(1/2)), -1))
	print(data.shape)