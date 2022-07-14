from email import message
from multiprocessing import context
from django.contrib import *
from django.shortcuts import render, redirect
from .forms import *

def All_Trainees(request):
    trainee= Trainee_model.objects.all()
    context={'all_T': trainee}
    return render(request, "all_Trainee.html", context)


def Trainee_save(request):
    if request.method == 'POST':
        form = T_Forms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = T_Forms()
    
    return render(request, "create.html", {'Trainee_s': form})

def Trainee_update(request, id):
    trainee= Trainee_model.objects.get(id=id)
    form = T_Forms (request.POST, instance=trainee)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, "update.html",{'Trainee_u': form})

def deleteTrainees(request, id):
    trainee= Trainee_model.objects.get(id=id)
    if request.method=='POST':
        trainee.delete()
       
        return redirect('/')
    return render(request, "delete.html") 
