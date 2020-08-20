import os
import logging
import numpy as np
from tensorflow import keras


def get_number(data):
	"""Takes array of values between 0 and 255 of length which can be divided by 784, 
	reshapes it to 28x28 and predicts number using neural network
	If something wrong, returns None"""
	if not isinstance(data, list):
		return None
	data = prepare(data)
	return predict(data)
	

def prepare(data):
	"""Reshapes data to 1x28x28 and makes all values floats between 0 and 1
	If something wrong, returns None"""
	if (len(data) % 784) != 0:
		return None
	try:
		data = np.array(data, dtype='float16')
		if np.isnan(data).any():
			return None
		data /= 255

		data = data.reshape((int(len(data)**(1/2))), (int(len(data)**(1/2))))
	except ValueError as err:
		print('Error in prepare:', err)
		return None
	
	if len(data) > 28:
		data = reduce_shape(data)

	return data


def reduce_shape(data):
	"""Reshapes data to 1x28x28
	If something wrong, returns None"""
	if (len(data) % 784) != 0:
		return None

	data28 = np.array([], dtype='float16')
	axelen = len(data)
	scale = axelen // 28
	
	for y in range(28):
		for x in range(28):
			data28 = np.append(data28, data[y*scale:y*scale+scale, x*scale:x*scale+scale].mean())
	try:
		data28 = data28.reshape((1, 28, 28))
	except ValueError as err:
		print('Error in reduce_shape:', err)
		return None
	
	return data28


def predict(data):
	"""Predicts a number from 1x28x28 dataset of float 0-1 values
	If something wrong, returns None"""
	if (not os.path.isfile('apps/nums/nn_model/saved_model.pb')) or (not os.path.isdir('apps/nums/nn_model/variables')):
		train_and_save()
	if not os.path.isdir('apps/nums/nn_model'):
		return None
	model = keras.models.load_model('apps/nums/nn_model')
	try:
		result = model.predict(data)
	except ValueError as err:
		print('Error in predict:', err)
		return None
	return np.argmax(result), result


def train_and_save():
	"""Creates model and saves it to apps/nums/nn_model directory"""
	if os.path.isdir('apps/nums/nn_model'):
		return
	mnist = keras.datasets.mnist.load_data()

	model = keras.models.Sequential([
		keras.layers.Flatten(input_shape=(28, 28)),
		keras.layers.Dense(128, activation='relu'),
		keras.layers.Dense(10, activation='softmax')
	])

	train_images = mnist[0][0] / 255.0
	train_labels = mnist[0][1]

	model.compile(
		optimizer='adam',
		loss='sparse_categorical_crossentropy',
		metrics=['accuracy']
	)

	model.fit(train_images, train_labels, epochs=6)
	model.save('apps/nums/nn_model')