from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1> Welcome to my music app</H1>")

def music(response):
    return HttpResponse("<h1> Welcome to my music page</H1>")