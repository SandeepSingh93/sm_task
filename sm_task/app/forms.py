from django import forms
from .models import Project,Task,Answer


QuestionChoice = (
    ('Multiple Choice','Multiple Choice'), ('Boolean Choice','Boolean Choice'), ('Rating scale','Rating scale'),
    ('Text/Paragraph','Text/Paragraph'), ('Number Input','Number Input'), ('Picture Input','Picture Input'),
)

SourceChoice = (
    ('1','Manually'),('2','Import CSV file'),
)


class TeacherForm(forms.ModelForm):
    Name = forms.CharField(label='Your Name')
    Description = forms.CharField(label='Description')
    NumberOfQuestions = forms.IntegerField(label='No. of questions')
    Source = forms.ChoiceField(label="How would you like provide data ",widget=forms.RadioSelect,choices=SourceChoice)
    File = forms.FileField(label="Choose file to upload(*Not Requied in manual mode)",required=False)
    class Meta:
        model= Project
        fields= '__all__'


class TaskForm(forms.ModelForm):
    Question = forms.CharField(label='Question',max_length=500,required=True)
    QuestionType = forms.ChoiceField(label='Question Type',choices=QuestionChoice)
    AnswerOptions = forms.CharField(label='Answer Option',)
    class Meta:
        model = Task
        fields= '__all__'


class StudentForm(forms.ModelForm):
    Answers = forms.CharField(label='Answer')
    class Meta:
        model=Answer
        fields='__all__'