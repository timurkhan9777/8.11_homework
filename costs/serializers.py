from rest_framework import serializers
from .models import DailyCosts

class DailyCostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCosts
        fields = '__all__'
