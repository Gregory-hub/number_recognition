import os
import shutil
import random
import numpy as np
from tensorflow import keras

from django.test import TestCase

from ..services import *


class TestGetNumber(TestCase):

	def test_valid_data(self):

		data = [random.randint(0, 255) for i in range(784*784)]
		result = get_number(data)
		self.assertTrue(isinstance(result[0], np.int64))
		self.assertTrue(isinstance(result[1], np.ndarray))


	def test_invalid_data(self):

		data = [random.randint(0, 255) for i in range(783)]
		result = get_number(data)
		self.assertEquals(result, None)

		data = [random.randint(0, 255) for i in range(785)]
		result = get_number(data)
		self.assertEquals(result, None)

		data = ['str' for i in range(784)]
		result = get_number(data)
		self.assertEquals(result, None)

		data = [None for i in range(784)]
		result = get_number(data)
		self.assertEquals(result, None)

		data = ['' for i in range(784)]
		result = get_number(data)
		self.assertEquals(result, None)

		data = [np.nan for i in range(784)]
		result = get_number(data)
		self.assertEquals(result, None)


class TestPrepare(TestCase):

	def test_valid_data(self):

		data = [random.randint(0, 255) for i in range(784*784)]
		result = prepare(data)

		self.assertEquals(result.shape, (1, 28, 28))
		self.assertEquals(result.dtype, np.float16)
		self.assertFalse(np.isnan(data).any())
		for y in result[0]:
			for x in y:
				self.assertTrue(x > 0 and x < 1)


	def test_invalid_data(self):
		data = [random.randint(0, 255) for i in range(783)]
		result = prepare(data)
		self.assertEquals(result, None)

		data = [random.randint(0, 255) for i in range(785)]
		result = prepare(data)
		self.assertEquals(result, None)

		data = ['str' for i in range(784)]
		result = prepare(data)
		self.assertEquals(result, None)

		data = [None for i in range(784)]
		result = prepare(data)
		self.assertEquals(result, None)

		data = ['' for i in range(784)]
		result = prepare(data)
		self.assertEquals(result, None)

		data = [np.nan for i in range(784)]
		result = prepare(data)
		self.assertEquals(result, None)


class TestReduceShape(TestCase):

	def test_valid_data(self):
		data = np.array([[random.random() for i in range(784)] for i in range(784)])
		result = reduce_shape(data)

		self.assertEquals(result.shape, (1, 28, 28))


	def test_invalid_data(self):
		data = np.array([[random.random() for i in range(784)] for i in range(783)])
		result = reduce_shape(data)
		self.assertEquals(result, None)

		data = np.array([[random.random() for i in range(784)] for i in range(785)])
		result = reduce_shape(data)
		self.assertEquals(result, None)


class TestPredict(TestCase):

	def test_model(self):
		mnist = keras.datasets.mnist.load_data()
		test_images, test_labels = mnist[1][0] / 255.0, mnist[1][1]

		results = []
		for i in range(100):
			result, probabilities = predict(test_images[i].reshape((1, 28, 28)))
			results.append(result == test_labels[i])
		self.assertTrue(results.count(True) / len(results) * 100 > 98.0)


class TestTrainAndSave(TestCase):

	def tearDown(self):
		shutil.rmtree('apps/nums/nn_model')

	def test_if_dir_doesnt_exist(self):
		if os.path.isdir('apps/nums/nn_model'):
			shutil.rmtree('apps/nums/nn_model')
		train_and_save()
		self.assertTrue(os.path.isdir('apps/nums/nn_model'))

	def test_if_dir_does_exist(self):
		if not os.path.isdir('apps/nums/nn_model'):
			os.mkdir('apps/nums/nn_model')
		train_and_save()
		self.assertTrue(os.path.isdir('apps/nums/nn_model'))