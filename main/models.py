from django.db import models

# Create your models here.


class Subject(models.Model):

    subj_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subj_name


class Question(models.Model):

    quest_name = models.CharField(max_length=200)
    related_subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return self.quest_name


class Answer(models.Model):

    ans_name = models.CharField(max_length=300)
    related_question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')

    def __str__(self):
        return self.ans_name

