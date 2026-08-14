from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello_spotify(request):
    return JsonResponse({"message": "Hello, Spotify Fans!"})
