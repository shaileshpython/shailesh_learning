from django.db import models
from .constants import JOB_ROLES
from datetime import datetime
# Create your models here.
default_time = datetime.strptime('00:00:00', '%H:%M:%S').time()

class Candidate(models.Model):
	name = models.CharField(max_length=30,db_index=True)
	username = models.CharField(max_length=20,unique=True,default="admin",db_index=True)
	role = models.CharField(db_index=True, choices=JOB_ROLES, default=JOB_ROLES[0][0], max_length=100)

	def __str__(self):
		return self.username

class AgentActivitybkTest(models.Model):
	username = models.CharField(max_length=50,default='')
	full_name = models.CharField(max_length=150,default='')
	supervisor_name = models.CharField(max_length=150,default='')
	campaign     =  models.CharField(max_length=150,default='')
	app_idle_time = models.TimeField(default=default_time, blank=True, null=True)
	ring_duration_avg = models.CharField(max_length=255, blank=True, null=True)
	date = models.DateField(auto_now_add=False, db_index=True,default=None,null=True)

#AgentActivitybkTest

# username='shailesh',full_name='', supervisor_name = '',campaign = 'test',app_idle_time = datetime.time(0, 0),
# ring_duration_avg = '00:00:06'
# date = '2022-12-15'





	

