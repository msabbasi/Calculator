from rest_framework import serializers
from django.core.validators import RegexValidator

from calculator.models import *


#class Serializer(ModelSerializer):
#	def get_instance(self):
#		return self.Meta.model(**self.validated_data)

#def default_serializer(model_class):
#	class _serializer(Serializer):
#		class Meta:
#			model = model_class
#			fields = [field.name for field in model_class._meta.fields]
#	return _serializer

letters = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')

class VariableSerializer(serializers.Serializer):
	variableName = serializers.CharField(validators=[letters])
	variableValue = serializers.FloatField()

