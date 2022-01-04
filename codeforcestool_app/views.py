from django.shortcuts import render
from django.core.mail import send_mail
import re 
import requests
import json


class contest_details():
    "Stores name and place pairs"
    def __init__(self, problem_name, rating,rating_percent):
        self.problem_name = problem_name
        self.rating = rating
        self.rating_percent = rating_percent


# Create your views here.
def index(request):
    
    response=requests.get("https://flaskapitesting.herokuapp.com/api/1616")
    print(response.status_code)
    # print(response.json())
    ls = response.json()
    lists = []
    for attribute, value in ls.items():
        varr = value
        varr = int(float(varr))
        lists.append(contest_details(attribute,value, (varr)//40))
    context = {
         "problem_name" : ['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J'],
    }
    contest_name = 'Codeforces Round 780 (Div 2)'
    return render(request,'index.html',{'contest_name':contest_name,'lists':lists})

def ourteam(request):
    return render(request,'ourteam.html',{})

def register(request):
    return render(request,'register.html',{})

def contactus(request):

    msg = ''
    if request.method == 'POST':
        first = request.POST.get('First')
        last = request.POST.get('Last')
        email = request.POST.get('Email')
        message = request.POST.get('Message')
        myemail = 'akhilsainiwork@gmail.com'

        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        else:
            message = 'Name : '+ first+' '+last +'\nEmail : '+email+'\nMessage : '+message
            send_mail('Message From Codeforces Tool',message,'',[myemail])
            msg = 'Your message have been sent successfully. Thank You.'

    return render(request,'contactus.html',{'msg':msg})



def iccc2020(request):
    return render(request,'iccc2020.html',{})
    