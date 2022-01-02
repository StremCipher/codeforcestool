from django.shortcuts import render

class contest_details():
    "Stores name and place pairs"
    def __init__(self, problem_name, rating,rating_percent):
        self.problem_name = problem_name
        self.rating = rating
        self.rating_percent = rating_percent


# Create your views here.
def index(request):
    
    lists = []
    lists.append(contest_details("A",800, 80000//4000))
    lists.append(contest_details("B",1200, 120000//4000))
    lists.append(contest_details("C",1800, 180000//4000))
    lists.append(contest_details("D",2400, 240000//4000))
    lists.append(contest_details("E",3000, 300000//4000))
    lists.append(contest_details("F",3600, 360000//4000))
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
    return render(request,'contactus.html',{})

def iccc2020(request):
    return render(request,'iccc2020.html',{})
    