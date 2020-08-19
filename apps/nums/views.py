import logging

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from .services import *


class IndexView(TemplateView):
	template_name = 'nums/index.html'


def canvas(request):
	"""Ajax view
	Takes array of length which can be divided by 784 and returns number
	""" 
	data = request.POST.get('data', default=None)

	number = None
	if data != None:
		data = data.replace('[', '').replace(']', '').split(',')
		if (len(data) % 784) == 0:
			number = get_number(data)

	print(number)

	return JsonResponse({'number': str(number)})