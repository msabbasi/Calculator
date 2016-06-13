from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from calculator.serializers import *

import calculation


class CalculationView(APIView):
	def post(self, request, *args, **kwargs):
		"""
		Post a calculation and receive the result back
		"""
		expression = request.data.get('expression', None)

		if expression and calculation.valid_syntax(expression):
			variables = request.session.get("variables", {})
			success, result = calculation.evaluate(expression, variables)
			if success:
				return Response({'result': result}, status=200)
			if 'too large' in result:
				print result * 3
				return Response({'error':result}, status=501)
							
		else:
			result = "invalid expression"
		return Response({'error':result}, status=400)

class VariablesView(APIView):
	def post(self, request, *args, **kwargs):
		"""
		Add or modify a variable. (var_name not required in the url)
		"""
		serializer = VariableSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		data = serializer.validated_data
		try:
			request.session['variables'].update({data['variableName'] : data['variableValue']})
		except KeyError:
			request.session['variables'] = {data['variableName'] : data['variableValue']}

		return Response(data, status=200)

	def get(self, request, var_name = None, *args, **kwargs):
		"""
		Get a variable or the whole list if variable name not specified
		"""
		variables = request.session.get("variables", {})
		if var_name:
			var_value = variables.get(str(var_name), None)
			return Response({var_name: var_value})
		variables = request.session.get("variables", {})
		return Response(variables)
