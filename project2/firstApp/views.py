from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    # return HttpResponse("This is our FirstApp Home Page")
    return render(request,'firstApp/home.html')
