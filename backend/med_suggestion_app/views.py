from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def maps(request):
    return render(request, 'maps.html')