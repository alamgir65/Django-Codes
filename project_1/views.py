from django.http import HttpResponse
def contact(request):
    return HttpResponse("This is Contact Page")

def home(request):
    return HttpResponse("This is Home Page")