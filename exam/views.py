from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, render
from .models import Contact
from django.contrib.auth import authenticate,login
from django.urls import reverse
from .models import Maths,English, Score,Demo,Essay
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):


    return render(request, "exam/index.html")

def exam_reg(request):


    return render(request, "exam/examrreg.html")


def contact(request):
    Name=request.POST['fullname']
    Email=request.POST['email']
    Message=request.POST['message']
    
    con=Contact(name=Name,email=Email,message=Message)
    con.save()

    return HttpResponseRedirect(reverse("home"))

def log(request):

    return render(request,"exam/login.html")

def user_login(request):
    name=request.POST["name"]
    password=request.POST["password"]
    user=authenticate(username=name,password=password)

    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('instruction'))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required(login_url="login")
def questions(request):
    maths=Maths.objects.all()

    context={
        "maths":maths
    }
    return render(request,"exam/questions.html",context)


@login_required(login_url="login")
def english(request):
    eng=English.objects.all()
    essay=Essay.objects.all()

    context={
        "eng":eng,
        "essay":essay
    }
    return render(request,"exam/engliah.html",context)


def demo(request):
    demo=Demo.objects.all()

    context={
        "demo":demo
    }
    return render(request,"exam/demo.html",context)


@login_required(login_url="login")  
def instruction(request):

    return render(request,"exam/instructions.html")


def savemscore(request):
    result=int(request.GET.get("tscore",False))
    score=Score(student=request.user,subject="mathematics",score=result)
    score.save()
    data={
        "result":result
    }
    
    return JsonResponse(data)

def saveescore(request):
    result=int(request.GET.get("tscore",False))
    score=Score(student=request.user,subject="english",score=result)
    score.save()
    data={
        "result":result
    }
    
    return JsonResponse(data)



