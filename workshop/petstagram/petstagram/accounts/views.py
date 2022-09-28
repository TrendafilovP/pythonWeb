from urllib import request
from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, template_name='accounts/')

def login(request):
    pass

def profile_details(request):
    pass

def profile_edit(request):
    pass

def profile_delete(request):
    return None