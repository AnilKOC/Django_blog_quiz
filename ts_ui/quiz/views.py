from django.shortcuts import render

from .models import Quiz,Question,Choice

def index(request):
    if request.method == 'POST':
        context = request.POST
        print(context)
        return render(request,'quiz/detail.html',context)
    context = {
        'quizs': Quiz.objects.all(),
        'questions' : Question.objects.all(),
        'choices': Choice.objects.all()
    }
    return render(request, 'quiz/quiz.html',context)
