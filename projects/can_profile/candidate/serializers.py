from rest_framework import serializers
from .models import *

class CandidateprofileSerializer(serializers.ModelSerializer):
	""" candidate Serializer for showing and saving the data"""
	class Meta:
		model = Candidate
		fields = '__all__'
		
