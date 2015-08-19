from django.contrib import admin

from .models import Project,Task,Answer
#from .forms import TeacherForm,TaskForm

class AppAdmin(admin.ModelAdmin):
    #form= TeacherForm,TaskForm
    class Meta:
        model= Project,Task,Answer

admin.site.register(Project,AppAdmin)
admin.site.register(Task,AppAdmin)
admin.site.register(Answer,AppAdmin)
