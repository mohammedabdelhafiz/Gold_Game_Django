from django.shortcuts import render, HttpResponse,redirect
import random

def index(request):
    if not 'totalgold' in request.session:
        request.session['totalgold']=0   #to reset and if i just i opened the page
    return render(request,'basic.html')

def calculate(request):
    if request.method == "POST":
        select=request.POST['building']
        if select==(("farm") or ("cave") or ("house")):
            rand=random.randint(10,20)
        else:
            rand=random.randint(0,50)
            rand2=random.randint(0,1)
            print(rand2)
            if rand2 ==0:
                print(request.session['totalgold'])
                request.session['totalgold']=int(request.session['totalgold'])-int(rand)
                print(request.session['totalgold'])
                return redirect('/Gold')
        print(rand)
        print(select)
        request.session['totalgold']=int(request.session['totalgold'])+int(rand)

    return redirect('/Gold')

def reset(request):
    del request.session['totalgold']
    return redirect('/Gold')