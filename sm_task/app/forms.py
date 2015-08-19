from django import forms
from .models import Project,Task

class TeacherForm(forms.ModelForm):
    Name = forms.CharField(label='Your Name',max_length=100,required=True)
    Description = forms.CharField(label='Description',max_length=500)
    NumberOfQuestions = forms.IntegerField(label='No. of questions',required=True)
    File = forms.FileField(label="Choose file to upload")

    class Meta:
        model= Project
        fields= '__all__'


QuestionChoice = (
    ('1','Multiple Choice'), ('2','Boolean Choice'), ('3','Rating scale'), ('4','Text/Paragraph'), ('5','Number Input'), ('6','Picture Input'),
)

def getType():
    return
class TaskForm(forms.ModelForm):
    Question = forms.CharField(label='Question',max_length=500,required=True)
    QuestionType = forms.ChoiceField(choices=QuestionChoice)
    #Options = forms.ChoiceField(choices=getType())
    class Meta:
        model = Task
        fields= '__all__'

class StudentForm(forms.ModelForm):
    pass