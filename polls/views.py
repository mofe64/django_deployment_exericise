from django.shortcuts import render
from .models import Question


# Create your views here.
def home(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'home.html', context)
