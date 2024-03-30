from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rohit(requst):
   return render(requst,'rohit.html')

def harshad(requst):
   return HttpResponse('harshad is a new player')