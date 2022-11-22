from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    return HttpResponse('Good Morning')

def wish(request):
    return HttpResponse('Have a Nice Day')