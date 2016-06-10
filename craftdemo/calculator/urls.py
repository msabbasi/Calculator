from django.conf.urls import patterns, url
from calculator.views import *

urlpatterns = [
	url(r'^addition/$', AdditionView.as_view(), name='addition'),
]
