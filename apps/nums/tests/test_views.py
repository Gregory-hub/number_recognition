import json
import random

from django.urls import reverse
from django.test import Client, TestCase


# class TestIndexView(TestCase):
	
	# def test_response(self):
	# 	url = reverse('nums:index')
	# 	response = self.client.get(url)
	# 	self.assertEquals(response.status_code, 200)


class TestCanvasView(TestCase):

	# def test_json_response_if_get(self):
	# 	url = reverse('nums:canvas')
	# 	response = self.client.get(url)
		# self.assertEquals(response.status_code, 404)

	def test_json_response_if_post(self):
		url = reverse('nums:canvas')
		data = [random.randint(0, 255) for i in range(784)]
		# print(data[-1])
		response = self.client.post(url, {'data': data})
		# self.assertEquals(response.status_code, 200)
		# self.assertTrue(isinstance(json.loads(response.content).get('number'), int))

	# def test_json_response_if_invalid_post_data(self):
	# 	url = reverse('nums:canvas')
	# 	response = self.client.post(url, {'data': ''})
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertEquals(json.loads(response.content).get('number'), None)

	# 	response = self.client.post(url, {'data': 'string'})
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertEquals(json.loads(response.content).get('number'), None)

	# 	response = self.client.post(url, {'data': 1})
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertEquals(json.loads(response.content).get('number'), None)

	# 	url = reverse('nums:canvas')
	# 	response = self.client.post(url)
	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertEquals(json.loads(response.content).get('number'), None)
