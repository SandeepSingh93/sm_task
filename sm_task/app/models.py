from django.db import models

class Project(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    NumberOfQuestions = models.IntegerField()

    def __unicode__(self):
        return self.Name

class Task(models.Model):
    Question = models.CharField(max_length=500)
    QuestionType = models.CharField(max_length=25)
    #QuestionOptions = models.CharField

    def __unicode__(self):
        return self.Question

class Answer(models.Model):
    Answers = models.CharField(max_length=500)

    def __unicode__(self):
        return self.Answers

