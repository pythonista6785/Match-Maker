from django.db import models


class Question(models.Model):
	text = models.TextField()
	acitve = models.BooleanField(default=True)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now = False)


	def __unicode__(self):
		return self.text