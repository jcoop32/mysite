from django.http import Http404
from django.shortcuts import render
from .models import Question
# Create your views here.

def index(request):
    # getting 5 most recent questions 
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # sending context to varibable in index.html
    context = {'latest_question_list': latest_question_list}
    # rendering screen with index.html and question list
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # try-catch block to see if question exists or not
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist: #throwing error if question doesnt exist
        raise Http404('Question does not exist')
    # rendering screen with detail.html and question
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response =  "You're looking at the results of %s."
    return HttpResponse(response % question_id) 

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

