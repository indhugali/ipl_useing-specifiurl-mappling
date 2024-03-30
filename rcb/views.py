from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(requst):
    return render(requst,'virat.html')

def maxwell(requst):
    return HttpResponse('maxwell is best batter')