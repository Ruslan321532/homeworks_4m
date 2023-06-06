from django.shortcuts import HttpResponse, redirect
import datetime


# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It's my project")


def redirect_to_youtube_view(request):
    if request.method == 'GET':
        return redirect("https://youtube.com")


def now_date_view(request):
    if request.method == 'GET':
        now = datetime.datetime.now()
    return HttpResponse(now)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")
