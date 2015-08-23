from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
import csv,os
from django.forms.formsets import formset_factory


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

        elif row[1]=="Rating Scale":
                data_to_insert.AnswerOptions=str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])

        elif row[1]=="Number Input":
            data_to_insert.AnswerOptions=str(row[2])+","+str(row[3])

        else:
            data_to_insert.AnswerOptions=row[2]

        data_to_insert.save()


def copy_to_temp(teacher):
    task_data = Task.objects.filter(TaskBy__Name=teacher)
    for x in task_data:
        temp = Temp()
        temp.TId= x.TId
        temp.TeacherName= x.TaskBy.Name
        temp.Question= x.Question
        temp.QuestionType = x.QuestionType
        temp.AnswerOptions = x.AnswerOptions
        temp.save()


def get_task(request):
    project = Project.objects.latest('PId')
    NumberOfTask = project.NumberOfQuestions
    TaskFormSet = formset_factory(TaskForm,extra=NumberOfTask)

    if request.method == "POST":
        formset= TaskFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                data_to_insert=form.save(commit=False)
                data_to_insert.TaskBy=Project.objects.latest('PId')
                data_to_insert.save()
            return HttpResponseRedirect('/student/')

    return render(request,"task.html",{'formset':TaskFormSet()})


teacher=""

def get_teachername(request):

    project_list = Project.objects.all()
    teacher_list=[]
    for x in project_list:
        teacher_list.append(x.Name)
    if request.method == "POST":
        global teacher
        teacher=request.POST.get('teachername')
        copy_to_temp(teacher)
        return HttpResponseRedirect('/studentanswer/')

    return render(request,"student.html",{'teacher_list':teacher_list})




def get_answers(request):

    question_list=Temp.objects.filter(TeacherName=teacher)

    if question_list[0].QuestionType == "Multiple Choice":
        form=StudentMultipleChoiceForm(request.user,request.POST)
    elif question_list[0].QuestionType == "Boolean Type":
        form=StudentBooleanChoiceForm(request.user,request.POST)
    elif question_list[0].QuestionType == "Rating Scale":
        form=StudentRatingScaleForm(request.user,request.POST)
    elif question_list[0].QuestionType == "Text/Paragraph":
        form=StudentParagraphForm(request.user,request.POST)
    elif question_list[0].QuestionType == "Number Input":
        form=StudentNumberInputForm(request.user,request.POST)
    # elif get_answers.question_list[0].QuestionType == "Picture Input":
    #     form=StudentPictureInputForm(request.user,request.POST)

    if request.method == "POST":
        if form.is_valid():
            data_to_insert=form.save(commit=False)
            ques=Task.objects.filter(TId=question_list[0].TId)
            data_to_insert.Question=ques[0]
            data_to_insert.save()
            TempInstance=Temp.objects.filter(TId=question_list[0].TId)
            TempInstance.delete()
            if Temp.objects.all().exists():
                return HttpResponseRedirect('/studentanswer')

            else:
                return HttpResponseRedirect('/thankyou')

    return render(request,"studentanswer.html",{'question_list':question_list,'form':form})


def thankyou(request):

    return render(request,"thankyou.html")
