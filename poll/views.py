from django.shortcuts import render
from .models import *
from django.contrib.auth.views import LoginView
from .forms import  LoginUserForm, ResultsForm
# Create your views here.
def polls(request):
    first = Poll.objects.all()
    return render(request,'poll/polls.html',{'first':first})

def show_poll(request,poll_id):
    poll =Poll.objects.get(id=poll_id)
    question = Question.objects.filter(poll_id=poll_id)
    return render(request,'poll/show_poll.html',{'poll':poll,'question':question})


def show_question(request,question_id):
    question = Question.objects.filter(id=question_id)
    answer = Answer.objects.filter(question=question_id)
    form = ResultsForm(request.POST or None)
    if form.is_valid():
        answer_save=form.cleaned_data.get('answer')
        if User.is_authenticated:
            user= request.user.username
        results_save=ResultsModel(answer = answer_save,question=question_id, user=user)
        results_save.save()
    return render(request,'poll/show_question.html',{'question':question,'answer':answer,'form':form})


class login(LoginView):
    template_name = 'poll/login.html'
    form_class = LoginUserForm
    success_url = '/'
    def get_success_url(self):
        return self.success_url