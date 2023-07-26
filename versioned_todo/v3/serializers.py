from rest_framework import serializers
from tasks.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        ref_name = 'TodoSerializerV3'
        