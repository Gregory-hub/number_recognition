import functools
import traceback

from django.http import JsonResponse, HttpResponse
from django.views.generic.base import TemplateView


def base_json_view(fn):
	@functools.wraps(fn)
	def inner(request, *args, **kwargs):
		try:
			return fn(request, *args, **kwargs)
		except Exception as e:
			print('\nError in {0}\n{1}'.format(fn.__name__, traceback.format_exc()))
			return JsonResponse({'data': None, 'probabilities': None})

	return inner


def base_service_view(fn):
	@functools.wraps(fn)
	def inner(request, *args, **kwargs):
		try:
			return fn(request, *args, **kwargs)
		except Exception as e:
			print('\nError in {0}\n{1}'.format(fn.__name__, traceback.format_exc()))
			return None

	return inner


class BaseTemplateView(TemplateView):

	def dispatch(self, request, *args, **kwargs):
		try:
			return super().dispatch(request, *args, **kwargs)
		except Exception as e:
			print('\nError in {0}\n{1}'.format(fn.__name__, traceback.format_exc()))
			return HttpResponse(status=500)