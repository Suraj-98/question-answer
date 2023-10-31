from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import  *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url="http://localhost:8000/signinpage")
def homepage(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    context = {}
    for question in questions:
        for answer in answers:
            if str(answer.question) == question.question:
                if str(question.question) in context:
                    context[str(question.question)].append(answer) 
                else:
                    context[str(question.question)] = [answer]
    return render(request,"home.html",{"context":context})

def signuppage(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/signinpage/")
 
    form = NewUserForm()    
    obj=User.objects.all()
    return render(request,"signup.html",{'form':form})
    
    
def signinpage(request):

    if request.method=='POST':
        form=CustomAuthenticationForm(request=request,data=request.POST)
        if form. is_valid():
            uname=form.cleaned_data["username"]
            pname=form.cleaned_data["password"]
            user=authenticate(username=uname,password=pname)
            if user is not None:
                login(request,user)
                return redirect("/homepage/")
    else:
        form=CustomAuthenticationForm()
    return render(request,"signinpage.html",{'form':form})


def signoutpage(request):
    logout(request)
    return redirect("http://localhost:8000/signinpage")

@login_required(login_url="http://localhost:8000/signinpage")
def create_question(request):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/homepage/")
    form=QuestionForm()
    return render(request,"createQuestion.html",{'form':form})

@login_required(login_url="http://localhost:8000/signinpage")
def create_answer_for_a_question(request,pk):
    if request.method=='POST':
        question = Question.objects.get(id=pk)
        form=AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            form.save()
            return redirect("/homepage/")
    form=AnswerForm()
    return render(request,"answer.html",{'form':form})

@login_required(login_url="http://localhost:8000/signinpage")
def like_answer(request,pk):
    answer = Answer.objects.get(id=pk)
    answer.like += 1
    answer.save()
    return redirect("/homepage/")
    