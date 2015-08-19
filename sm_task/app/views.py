from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TeacherForm,TaskForm,StudentForm

def get_project(request):
    if request.POST:
        form = TeacherForm(request.POST)
        if form.is_valid():
            save_project=form.save(commit=False)
            save_project.save()
            return HttpResponseRedirect('/task/')
    else:
        form=TeacherForm()
    return render(request,'teacher.html',{'form':form})

def get_task(request):
    form= TaskForm(request.POST or None)
    if form.is_valid():
        save_task=form.save(commit=False)
        save_task.save()
    return render(request,"task.html",{'form':form})

def get_answers(request):
    form= StudentForm(request.POST or None)
    if form.is_valid():
        save_answer=form.save(commit=False)
        save_answer.save()
    return render(request,"student.html",{'form':form})