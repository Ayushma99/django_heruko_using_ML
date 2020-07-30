from rest_framework import serializers
from . models import approval
class api(serializers.ModelSerializer):
    class Meta:
        model=approval
        fields='__all__'
