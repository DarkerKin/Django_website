from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


rooms = [
    {'id':1, 'name':'Lets Learn python!'},
    {'id':2, 'name':'Design With Me!'},   
    {'id':3, 'name':'Frontend Developers'},    
]

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html') 
