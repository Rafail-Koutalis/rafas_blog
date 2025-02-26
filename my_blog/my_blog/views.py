from django.shortcuts import render



    
def homepage(request) :
    return render(request,'homepage.html')
    
def apps(request) :
    return render(request,'apps.html') 