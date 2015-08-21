from django.contrib import admin
from .models import Project,Task,Answer


class ProjectAdmin(admin.ModelAdmin):
    list_display= ('PId','Name','Description','NumberOfQuestions','File',)
    class Meta:
        model= Project


class TaskAdmin(admin.ModelAdmin):
    list_display= ('TId','TaskBy','Question','QuestionType','AnswerOptions',)
    class Meta:
        model= Task


class AnswerAdmin(admin.ModelAdmin):
    list_display= ('AId','Answers',)
    class Meta:
        model= Answer


admin.site.register(Project,ProjectAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Answer,AnswerAdmin)
