from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TeacherForm,TaskForm,StudentForm
from .models import Task,Project
import csv,os


def get_project(request):

    if request.method == "POST":
        form = TeacherForm(request.POST,request.FILES)

        if form.is_valid():
            source=form.cleaned_data['Source']

            if source=='2':

                if not bool(request.FILES):
                    return render(request,'teacher.html',{'form':form})

                form.save()
                file_name=request.FILES['File']
                save_from_csv(file_name)
                return HttpResponseRedirect('/student/')

            else:
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/task/')

    else:
        form=TeacherForm()

    return render(request,'teacher.html',{'form':form})


def save_from_csv(file_name):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_file_dir = str(os.path.join(os.path.dirname(BASE_DIR),"userfiles")) + "/" + str(file_name)
    records = csv.reader(open(csv_file_dir),delimiter=',')

    for row in records:
        data_to_insert=Task()
        data_to_insert.TaskBy=Project.objects.latest('PId')
        data_to_insert.Question=row[0]
        data_to_insert.QuestionType=row[1]

        if row[1]=="Multiple Choice":
            data_to_insert.AnswerOptions=str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])

        elif row[1]=="Boolean Type":
            data_to_insert.AnswerOptions=str(row[2])+","+str(row[3])

        else:
            data_to_insert.AnswerOptions=row[2]

        data_to_insert.save()



def get_task(request):

    form= TaskForm(request.POST or None)

    if form.is_valid():
        save_task=form.save(commit=False)
        save_task.save()

    return render(request,"task.html",{'form':form})



def get_answers(request):

    form= StudentForm(request.POST or None)
    question_list=Task.objects.all()
    print(question_list)

    if form.is_valid():
        save_answer=form.save(commit=False)
        save_answer.save()

    return render(request,"student.html",{'form':form})