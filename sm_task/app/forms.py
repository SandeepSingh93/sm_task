from django import forms
from django.core.validators import *
from .models import *


QuestionChoice = (
    ('Multiple Choice','Multiple Choice'), ('Boolean Type','Boolean Type'), ('Rating Scale','Rating Scale'),
    ('Text/Paragraph','Text/Paragraph'), ('Number Input','Number Input'), ('Picture Input','Picture Input'),
)

SourceChoice = (
    ('1','Manually'),('2','Import CSV file'),
)


class TeacherForm(forms.ModelForm):
    Name = forms.CharField(label='Teacher Name')
    Description = forms.CharField(label='Task Description')
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
        fields= ['Question','QuestionType','AnswerOptions']


class StudentMultipleChoiceForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(StudentMultipleChoiceForm, self).__init__(*args, **kwargs)
        teacher = Temp.objects.latest('TeacherName')
        question_list=list(Temp.objects.filter(TeacherName=teacher.TeacherName))
        choice=question_list[0].AnswerOptions.split(',')
        MultipleChoice =(
            (choice[0],choice[0]),(choice[1],choice[1]),(choice[2],choice[2]),(choice[3],choice[3]),
        )
        self.fields['Answers'] = forms.ChoiceField(label="Answer",widget=forms.RadioSelect,choices= MultipleChoice)
    class Meta:
        model=Answer
        fields=['Answers']

class StudentBooleanChoiceForm(forms.ModelForm):
    def __init__(self, user,*args, **kwargs):
        super(StudentBooleanChoiceForm, self).__init__(*args, **kwargs)
        teacher = Temp.objects.latest('TeacherName')
        question_list=list(Temp.objects.filter(TeacherName=teacher.TeacherName))
        choice=question_list[0].AnswerOptions.split(',')
        MultipleChoice =(
            (choice[0],choice[0]),(choice[1],choice[1]),
        )
        self.fields['Answers'] = forms.ChoiceField(label="Answer",widget=forms.RadioSelect,choices= MultipleChoice)
    class Meta:
        model=Answer
        fields=['Answers']

class StudentRatingScaleForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(StudentRatingScaleForm, self).__init__(*args, **kwargs)
        teacher = Temp.objects.latest('TeacherName')
        question_list=list(Temp.objects.filter(TeacherName=teacher.TeacherName))
        ratings=question_list[0].AnswerOptions.split(',')
        RatingChoice = []
        for i in range(0,len(ratings)):
            RatingChoice.append((ratings[i],ratings[i]))
        self.fields['Answers'] = forms.ChoiceField(label="Answer",widget=forms.RadioSelect,choices= RatingChoice)
    class Meta:
        model=Answer
        fields=['Answers']

class StudentParagraphForm(forms.ModelForm):
    def __init__(self,user, *args, **kwargs):
        super(StudentParagraphForm, self).__init__(*args, **kwargs)
        teacher = Temp.objects.latest('TeacherName')
        question_list=list(Temp.objects.filter(TeacherName=teacher.TeacherName))
        max_characters=question_list[0].AnswerOptions
        self.fields['Answers'] = forms.CharField(label="Answer",widget=forms.Textarea,max_length=int(max_characters))
    class Meta:
        model=Answer
        fields=['Answers']

class StudentNumberInputForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(StudentNumberInputForm, self).__init__(*args, **kwargs)
        teacher = Temp.objects.latest('TeacherName')
        question_list=list(Temp.objects.filter(TeacherName=teacher.TeacherName))
        number_range=question_list[0].AnswerOptions.split(',')
        self.fields['Answers'] = forms.IntegerField(label="Answer",validators=[MaxValueValidator(int(number_range[1])),
            MinValueValidator((int(number_range[0])))])
    class Meta:
        model=Answer
        fields=['Answers']

# class StudentPictureInputForm(forms.ModelForm):
#     def __init__(self, user,question_list, *args, **kwargs):
#         super(StudentPictureInputForm, self).__init__(*args, **kwargs)
#
#         self.fields['Choice'] = forms.
#     class Meta:
#         model=Answer
#         fields=[]

