from django.shortcuts import render
from django.http import  JsonResponse
from rest_framework.views import APIView
from .models import *
from .encrypt import *


# Create your views here.
#url :- /api/v1/expensesbyteam/{team_id}
class TeamExpenses(APIView):
	def post(self,request,*args, **kwargs):
		data = request.data
		# data['body'] = encrypt(data['body'],data['key'])
		# print(data['body'],"encrypted form id")
		team_id = decrypt(data['body'],data['key'])
		context = {}
		users_ids = list(TeamDetails.objects.filter(team_id=team_id).values_list("user_id",flat=True))
		expenses = list(Expenses.objects.filter(user__in=users_ids).values_list("amount",flat=True))
		total = sum(expenses)
		context['team_expenses'] =    total               #expenses of all users within a team
		return JsonResponse(context)

