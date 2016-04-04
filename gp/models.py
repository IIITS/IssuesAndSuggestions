from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Domain(models.Model):
	name = models.CharField(max_length = 100, primary_key=True)
	description = models.TextField()
	Incharge = models.TextField()
	def __str__(self):
		return self.name

class group(models.Model):
	name = models.TextField()


class UserProfile(models.Model):
	GENDER = (('M','Male'),('F','Female'),)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	gender = models.CharField(max_length=2,choices=GENDER)
	groupset = models.TextField()


class Complaint(models.Model):
	STATUS = (('Registered','Registered'),('Assigned','Assigned'),('Solved','Solved'),('Closed','Closed'),)
	title = models.CharField(max_length=200)
	description = models.TextField()
	domain = models.ForeignKey(Domain, on_delete = models.CASCADE)
	posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
	upvotes = models.PositiveIntegerField(default = 0)
	#downvotes = models.PositiveIntegerField(default = 0)
	status = models.CharField(max_length = 30,choices = STATUS,default = 'Registered')
	who_can_see = models.CharField(max_length = 2,choices = (('All','Everybody'),('F','Faculty')))
	solved  = models.BooleanField(default = False)
	approved = models.BooleanField( default= False)
	posted_on = models.DateTimeField(auto_now = True)
	def __str__(self):
			return str(self.title)

	def upvote(self):
		self.upvotes +=1
		return self.upvotes	

	def getUpvotes(self):
		return self.upvotes	

class Solution(models.Model):
	complaint = models.ForeignKey(Complaint, on_delete = models.CASCADE)
	solution = models.TextField()
	author = models.ForeignKey(User)
	given_on = models.DateTimeField(auto_now = True)

class Suggestion(models.Model):
	complaint = models.ForeignKey(Complaint,on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	suggestion = models.TextField()	
	upvotes = models.PositiveIntegerField()
	downvotes = models.PositiveIntegerField()


class Upvote(models.Model):
	cid = models.ForeignKey(Complaint, on_delete = models.CASCADE)
	uid = models.ForeignKey(User, on_delete = models.CASCADE)

	class Meta:
		unique_together = ('cid','uid')


class Notes(models.Model):
	code = models.CharField(db_index=True, max_length=20)
	Note = models.TextField()
	def __str__(self):
		return self.code		



