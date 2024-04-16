from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
# def main(request):
#     dic = {
#         'name': 'Alamgir Hossain Drubo',
#         'age': 22,
#         'University': 'National University',
#     }
#     return render(request, 'firstApp/index.html',dic)

def about(request):
    return render(request, 'firstApp/about.html')

def contact(request):
    return render(request, 'firstApp/contact.html')

def filtering(request):
    dic = {
        'name': 'Alamgir Hossain Drubo',
        'age': 22,
        'University': 'National University',
        'lst': [2,35,78.3,62],
        'birthdate': datetime.datetime.now(),
        'empty': False,
        'arr' : [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},],
        'chars' : ['a', 'b', 'c', 'd', 'e', 'f'],
        'unorder_lst' : ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
    }
    return render(request, 'firstApp/filtering.html',dic)