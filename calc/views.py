from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'A',
        'title': 'B',
        'content':'C',
        'date':'D, 2012',
        'titles':'django'
    },
    {
        'author': 'E',
        'title': 'F',
        'content':'G',
        'date':'H, 2020'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render( request,'home.html',context)

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    sum=val1+val2
    return render(request, 'result.html',{'sum1':sum})