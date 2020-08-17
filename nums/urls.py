from django.urls import path

from .urls import *


app_name = 'nums'
urlpatterns = [
	path('', canvas, name='canvas'),
]