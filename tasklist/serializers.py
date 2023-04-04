from rest_framework import serializers
from tasklist.models import tasklist


class tasklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasklist
        fields = '__all__'
