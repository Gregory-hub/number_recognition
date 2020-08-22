import logging
import functools
import traceback

from django.http import JsonResponse, HttpResponse
from django.views.generic.base import TemplateView


logger = logging.getLogger(__name__)


def base_json_view(fn):
	@functools.wraps(fn)
	def inner(request, *args, **kwargs):
		try:
			return fn(request, *args, **kwargs)
		except Exception as e:
			logger.error(traceback.format_exc())
			return JsonResponse({'data': None, 'probabilities': None})

	return inner


def base_service(fn):
	@functools.wraps(fn)
	def inner(*args, **kwargs):
		try:
			return fn(*args, **kwargs)
		except Exception as e:
			logger.error(traceback.format_exc())
			return None

	return inner


class BaseTemplateView(TemplateView):

	def dispatch(self, request, *args, **kwargs):
		try:
			return super().dispatch(request, *args, **kwargs)
		except Exception as e:
			logger.error(traceback.format_exc())
			return HttpResponse(status=500)