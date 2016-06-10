from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from calculator.serializers import *
# Create your views here.


class AdditionView(APIView):
	def post(self, request, *args, **kwargs):
		firstNum = request.data.get('firstNum', None)
		secondNum = request.data.get('secondNum', None)		
		return Response({firstNum + secondNum})

class SubtractionView(APIView):
	def post(self, request, *args, **kwargs):
		firstNum = request.data.get('firstNum', None)
		secondNum = request.data.get('secondNum', None)		
		return Response({firstNum - secondNum})

class MultiplicationView(APIView):
	def post(self, request, *args, **kwargs):
		firstNum = request.data.get('firstNum', None)
		secondNum = request.data.get('secondNum', None)		
		return Response({firstNum * secondNum})

class DivisionView(APIView):
	def post(self, request, *args, **kwargs):
		firstNum = request.data.get('firstNum', None)
		secondNum = request.data.get('secondNum', None)		
		return Response({firstNum / secondNum})

class CalculationView(APIView):
	def post(self, request, *args, **kwargs):
		expression = request.data.get('expression', None)
		result = 5
		return Response({result})

