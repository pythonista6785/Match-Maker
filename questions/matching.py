from decimal import Decimal

from django.contrib.auth import get_user_model

from questions.models import UserAnswer

User = get_user_model()

users = User.objects.all() #[user1, user2]

all_user_answers = UserAnswer.objects.all().order_by("user__id")  #[useranswer1, useranswer2]

admin = users[0]
vishwa = users[1]

UserAnswer.objects.filter(user=admin)
admin.useranswer_set.all()

UserAnswer.objects.filter(user=vishwa)
vishwa.useranswer_set.all()

a_answer1 = admin.useranswer_set.all()[0]
v_answer1 = vishwa.useranswer_set.all()[0]


a_answer1.question.id == v_answer1.question.id

a_answer = a_answer1.my_answer

a_pref = a_answer1.their_answer

v_answer = v_answer1.my_answer

v_pref = v_answer1.their_answer

a_answer = v_pref
a_pref = v_answer


def get_match(user_a, user_b):
	user_a_answers = UserAnswer.objects.filter(user=user_a)[0]
	user_b_answers = UserAnswer.objects.filter(user=user_b)[0]
	if user_a_answers.question.id == user_b_answers.question.id:
		user_a_answer = user_a_answers.my_answer
		user_a_pref = user_a_answers.their_answer
		user_b_answer = user_b_answers.my_answer
		user_b_pref = user_b_answers.their_answer
		user_a_total_awarded = 0
		user_b_total_awarded = 0
		if user_a_answer == user_b_pref:
			user_b_total_awarded += user_b_answers.their_points 
			print "%s a fits with user %s's preference"%(user_a_answers.user.username, user_b_answers.user.username )
		if user_a_pref == user_b_answer:
			user_a_total_awarded += user_a_answers.their_points
			print "user %s fits with user %s's preference" %(user_a_answers.user.username, user_b_answers.user.username )
		if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
			print "this is an ideal answer for both"
		print user_a, user_a_total_awarded, user_b
		print user_b, user_b_total_awarded, user_a
get_match(admin, vishwa)




def get_points(user_a, user_b):
	a_answers = UserAnswer.objects.filter(user=user_a)[0]
	b_answers = UserAnswer.objects.filter(user=user_b)[0]
	a_total_awarded = 0
	a_points_possible = 0
	if a_answers.question.id == b_answers.question.id:
		a_pref = a_answers.their_answer
		b_answer = b_answers.my_answer
		if a_pref == b_answer:
			'''
			awards points for correct answer
			'''
			a_total_awarded += a_answers.their_points
		'''
		assigning total points
		'''
		a_points_possible += a_answers.their_points
	print "%s has awarded %s points to %s" %(user_a, a_total_awarded, user_b)

get_points(admin, vishwa)







