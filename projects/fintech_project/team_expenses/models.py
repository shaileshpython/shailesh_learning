from django.db import models

# Create your models here.
class User(models.Model):
	""" This table will store the user information """
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100,null=True, blank=True,unique=True)
	
	def __str__(self):
		return self.name

class Expenses(models.Model):
	""" This table will store the expenses information """
	name = models.CharField(max_length=50)
	amount = models.FloatField()
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

class Team(models.Model):
	title = models.CharField(max_length=50)

	# def __str__(self):
	# 	return self.id

class TeamDetails(models.Model):
	team_id = models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)
	user_id = models.ManyToManyField(User, related_name='user_teamdetails',
			null=True, blank=True)

	# def __str__(self):
	# 	return str(self.numeric)

	# def __str__(self):
	# 	team = list(TeamDetails.objects.filter(team_id=self.team_id).values_list("team_id__title",flat=True))
	# 	return str(team[0])

# class user_id
