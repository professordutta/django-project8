from rest_framework import serializers
from .models import Mriic

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mriic
        fields = ['emp_id', 'emp_name', 'emp_age']
