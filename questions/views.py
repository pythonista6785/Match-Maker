from django.shortcuts import render, Http404

from .models import Question
from .forms import UserResponseForm

def home(request):
	if request.user.is_authenticated():
		form = UserResponseForm(request.POST or None)
		if form.is_valid():
			print form.cleaned_data
		queryset = Question.objects.all().order_by('-timestamp')
		print queryset
		instance =  queryset[0] 
		print instance
		context = {
			"form": form,
			"instance": instance,
			#"queryset": queryset
		}
		return render(request, "questions/home.html", context)
	else:
		raise Http404





