from django.db import models
from django.conf import settings


class Question(models.Model):
	text = models.TextField()
	acitve = models.BooleanField(default=True)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)
	#answer = models.ManyToManyField('Answer')


	def __unicode__(self):
		return self.text[:10]

class Answer(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=120)
	acitve = models.BooleanField(default=True)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)

	def __unicode__(self):
		return self.text[:10]


LEVELS = (
		('Mandatory', 'Mandatory'),
		('Very Important', 'Very Important'),
		('Somewhat Important', 'Somewhat Important'),
		('Not Important','Not Important'),
		)


class UserAnswer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	question = models.ForeignKey(Question)
	my_answer = models.ForeignKey(Answer, related_name='user_answer')
	my_answer_importance = models.CharField(max_length=50, choices=LEVELS)
	their_answer = models.ForeignKey(Answer, blank=True, null=True, related_name='match_answer')
	their_answer_importance = models.CharField(max_length=50, choices=LEVELS)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)
 


	def __unicode__(self):
		return self.my_answer.text[:10]