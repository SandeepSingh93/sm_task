from django.db import models

class Project(models.Model):
    PId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=35)
    Description = models.CharField(max_length=150)
    NumberOfQuestions = models.IntegerField()
    File = models.FileField(upload_to='.')

    def __unicode__(self):
        return self.Name

class Task(models.Model):
    TId= models.AutoField(primary_key=True)
    Question = models.CharField(max_length=100)
    QuestionType = models.CharField(max_length=15)
    AnswerOptions = models.CharField(max_length=100)

    def __unicode__(self):
        return self.Question

class Answer(models.Model):
    AId = models.AutoField(primary_key=True)
    Answers = models.CharField(max_length=500)

    def __unicode__(self):
        return self.Answers

