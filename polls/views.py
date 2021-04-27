from django.shortcuts import render, HttpResponse
from .models import Question
from decouple import config


# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'home.html', context)


def env(request):
    return HttpResponse(config('ENVIRONMENT'))
