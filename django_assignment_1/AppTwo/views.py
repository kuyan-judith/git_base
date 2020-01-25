from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
    context_dict={'content':'<em>this is appTwo!</em>'}
    return HttpResponse('<em>this is appTwo!</em>')

# Create your views here.
