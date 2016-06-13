from django.conf.urls import patterns, url
from calculator.views import *

urlpatterns = [
	url(r'^calculation/?$', CalculationView.as_view(), name='calculation'),
	url(r'^variables/(?P<var_name>.*)/?$', VariablesView.as_view(), name='variables'),
]
