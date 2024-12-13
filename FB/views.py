from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404,HttpRequest,HttpResponse,HttpResponseBadRequest
from django.template import loader
from django.contrib import messages
from django import middleware
from . models import MODELS
from . forms import FORMS


# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request = request))

def create(request):
    form = FORMS()
    context = {'forms':form}
    template = loader.get_template('create.html')
    return HttpResponse(template.render(request = request, context = context))

gmail = []
id = []
firstname = []
lastname = []


def database(request):
    if request.GET["id"] and request.GET["First_Name"] and request.GET["Last_Name"] and request.GET["Gmail"]:
        if request.GET["Gmail"] in gmail:
            return HttpResponse(f"{request.GET["Gmail"]} already exists")
        
        gmail.append(request.GET["Gmail"])
        id.append(request.GET["id"])
        firstname.append(request.GET["First_Name"])
        lastname.append(request.GET["Last_Name"])
        print(id,firstname,lastname,gmail)
        return HttpResponse(f"{request.GET["First_Name"]} {request.GET["Last_Name"]} created")