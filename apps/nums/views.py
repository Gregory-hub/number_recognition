import logging
import sys

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .services import *
from .base import base_json_view, BaseTemplateView


class IndexView(BaseTemplateView):
	template_name = 'nums/index.html'


@base_json_view
def canvas(request):
	"""Ajax view
	Takes array of length which can be divided by 784 and returns number
	""" 
	if request.method == 'POST':
		data = request.POST.get('data', default=None)

		number = None
		probabilities = None
		if data:
			data = data.replace('[', '').replace(']', '').split(',')
			if (len(data) % 784) == 0:
				result = get_number(data)
				if result:
					number, probabilities = result

		return JsonResponse({'number': str(number), 'probabilities': str(probabilities)})

	else:
		return HttpResponse(status=404)
