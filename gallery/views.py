from django.shortcuts import render
from django.http import HttpResponse

# Initial index view for the gallery
def index(request):
    return HttpResponse("Welcome to the Gallery! It is currently under \
    construction. Please come back soon!")
