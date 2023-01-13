from .models import Candidate
# JsonResponse
from django.http import JsonResponse
def candidate_validation(function):
	"""
	This validation is used to do validation of
	candidate is already exist or not with same username
	at the time of candidate profile  creation
	"""
	def wrap(request, *args, **kwargs):
		username = request.POST.get('username')
		if Candidate.objects.filter(username__iexact=username.strip()).exists():
			return JsonResponse({"username_error": "Candidate with this username already exists"},status=500)
		# if .objects.filter(domain__iexact=domain.strip()).exists():
		# 	return JsonResponse({"client_domain_error": "Client with this domain already exists"},status=500)
		return function(request, *args, **kwargs)
	return wrap
