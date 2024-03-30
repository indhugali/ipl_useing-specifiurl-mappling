from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def msd(requst):
    return render(requst,'msd.html')


def jadaja(requst):
    return HttpResponse('jadaja is a best allrounder')