from django.forms import ModelForm
from . import models


class SubjectForm(ModelForm):

    class Meta:
        model = models.Subject
        fields = '__all__'


class QuestionForm(ModelForm):

    class Meta:
        model = models.Question
        fields = ['quest_name']


class AnswerForm(ModelForm):

    class Meta:
        model = models.Answer
        fields = ['ans_name']