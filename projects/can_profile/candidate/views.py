from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
# from .models import *
from .models import Candidate
from .serializers import CandidateprofileSerializer
from .constants import JOB_ROLES
from .utility import candidate_validation
from django.utils.decorators import method_decorator

@method_decorator(candidate_validation,name='post')
class Candidateprofile(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'base.html'

	def get(self,request):
		try:
			roles = JOB_ROLES
			return Response({"roles":roles})
		except Exception as e:
			print("Exception From Candidateprofile get method",e)

	def post(self,request):
		try:
			candidate_serializer = CandidateprofileSerializer(data=request.POST)
			if candidate_serializer.is_valid():
				candidate_serializer.save()
				msg = 'data saved successfully'
				return Response({'msg':msg})
			else:
				# print("error at candidate serializer",candidate_serializer.errors)
				return Response({"error":candidate_serializer.errors})
		except Exception as e:
			print("Exception From Candidateprofile get method",e)
			