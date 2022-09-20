from django.shortcuts import render, redirect, reverse
from . import models, forms
from django.views import generic
from django.http import HttpResponseRedirect
from django.db import IntegrityError


# Create your views here.


class Subjects(generic.ListView):
    template_name = 'subjects.html'
    model = models.Subject
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        ctxt = super(Subjects, self).get_context_data()
        ctxt['form'] = forms.SubjectForm()
        return ctxt

    def post(self,request):
        try:
            new_subj = models.Subject(subj_name=self.request.POST.get('subj_name'))
            new_subj.save()
            return redirect('/')
        except IntegrityError:
            return render(self.request,'no_result_page.html')


class QuestionsOfSubj(generic.DetailView):
    template_name = 'questions.html'
    model = models.Subject
    context_object_name = 'Subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = forms.QuestionForm()
        return context

    def post(self, request, pk):
        try:
            new_question = models.Question(
                quest_name=request.POST.get('quest_name'),
                related_subject=self.get_object())
            new_question.save()
            return redirect('main:questions', pk=pk)
        except IntegrityError:
            return render(self.request, 'no_result_page.html')


class AnswersOfQuestion(generic.DetailView):

    template_name = 'answer.html'
    model = models.Question
    context_object_name = 'Question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = forms.AnswerForm()
        return context

    def post(self, request, pk):
        try:
            new_answer = models.Answer(
                related_question=self.get_object(),
                ans_name=request.POST.get('ans_name'))
            new_answer.save()
            return redirect('main:answers', pk=pk)
        except IntegrityError:
            return render(self.request, 'no_result_page.html')


class CreateQuestion(generic.CreateView):

    model = models.Question
    fields = '__all__'
    template_name = 'question_Create.html'

    def get_success_url(self):
        return reverse('main:questions', kwargs={'pk': self.object.related_subject.pk})


class CreateAnswer(generic.CreateView):

    model = models.Answer
    fields = '__all__'
    template_name = 'answer_create.html'

    def get_success_url(self):
        return reverse('main:answers', kwargs={'pk': self.object.related_question.pk})


class EditAnswer(generic.UpdateView):

    template_name = 'editAns.html'
    model = models.Answer
    fields = '__all__'

    def get_success_url(self):
        return reverse('main:answers', kwargs={'pk': self.object.related_question.pk})


class EditQuestion(generic.UpdateView):

    template_name = 'edit_quest.html'
    model = models.Question
    fields = '__all__'

    def get_success_url(self):
        return reverse('main:questions', kwargs={'pk': self.object.related_subject.pk})


class EditSubject(generic.UpdateView):

    template_name = 'edit_subj.html'
    model = models.Subject
    fields = '__all__'
    success_url = '/'


class DeleteQuestion(generic.DeleteView):

    template_name = 'del_quest.html'
    model = models.Question

    def get_success_url(self):
        return reverse('main:questions', kwargs={'pk': self.object.related_subject.pk})


class DeleteSubject(generic.DeleteView):

    template_name = 'del_subj.html'
    model = models.Subject
    success_url = '/'


def del_ans(request, pk):
    ans_to_delete = models.Answer.objects.get(pk=pk)
    ans_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    search_input = request.GET.get('quest_name') or ''
    if search_input:
        try:
            queryset = models.Question.objects.filter(quest_name__iexact=search_input)
            return redirect('main:answers', pk=queryset.first().pk)
        except AttributeError:
            return render(request, 'no_result_page.html')

