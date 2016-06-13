from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory


# Create your tests here.

#factory = APIRequestFactory()
#request = factory.post('/notes/', {'title': 'new idea'})
#response = view(request)


#response = self.client.get('/users/4/')
#self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})

#view = UserDetail.as_view()
#request = factory.get('/users/4')
#response = view(request, pk='4')
#response.render()  # Cannot access `response.content` without this.
#self.assertEqual(response.content, '{"username": "lauren", "id": 4}')

class CalculationTests(APITestCase):
	def test_simple_calculation(self):
		"""
		Ensure we can evaluate a simple expression
		"""
		url = reverse('calculation')
		data = {'expression': '2+3*(4+2)'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, {'result': 20 })

	def test_invalid_calculation(self):
		"""
		Ensure we get a proper response for an invalid expression
		"""
		url = reverse('calculation')
		data = {'expression': '2+3**(4+2)'}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(response.data, {'error': 'invalid expression' })

class VariablesTests(APITestCase):
	def setUp(self):
		s = self.client.session
		s['variables'] = {'b': 567, 'c': 936}
		s.save()

	def test_retrieving_variables(self):
		"""
		Ensure we can retrieve memoory variables
		"""
		url = reverse('variables', args = ('b'))
		response = self.client.get(url, format='json')
		self.assertEqual(response.data, {'b': 567})
		
	def test_adding_variable(self):
		"""
		Ensure we can add a memory variable
		"""
		url = reverse('variables')
		data = {'variableName': 'a', 'variableValue': 123}
		response = self.client.post(url, data, format='json')
		s = self.client.session
		self.assertEqual(s['variables'],  {'a': 123, 'b':567, 'c': 936})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, {'variableName': 'a', 'variableValue': 123})
