from rest_framework.serializers import ModelSerializer

from calculator.models import *


class Serializer(ModelSerializer):
	def get_instance(self):
		return self.Meta.model(**self.validated_data)

def default_serializer(model_class):
	class _serializer(Serializer):
		class Meta:
			model = model_class
			fields = [field.name for field in model_class._meta.fields]

	return _serializer
