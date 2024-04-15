from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    dic = {'Author' : 'Alamgir', 'Age': 10, 'lst': ['python','is','best'],
        'birthday': datetime.datetime.now(), 'value': '',     'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'description' : 'Python is a high-level, interpreted, interactive, object-oriented programming language.'
        },
        {
            'id' : 2,
            'name' : 'Django',
            'description' : 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.'
        },
        {
            'id' : 3,
            'name' : 'Flask',
            'description' : 'Flask is a Python web framework that encourages rapid development and clean, pragmatic design.'
        },
    ]}
    return render(request, 'firstApp/home.html',dic)
