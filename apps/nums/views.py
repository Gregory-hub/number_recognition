import logging

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
	template_name = 'nums/index.html'


def canvas(request):

	data = request.POST.get('data', default=None)

	data = data.replace('[', '').replace(']', '').split(',')
	print(data[:10])

	return JsonResponse({'data': data})