from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('',views.Subjects.as_view(),name='subjects'),
    path('subject_questions/<int:pk>',views.QuestionsOfSubj.as_view(),name='questions'),
    path('question_answers/<int:pk>',views.AnswersOfQuestion.as_view(),name='answers'),
    path('<int:pk>/edit_ans',views.EditAnswer.as_view(),name='edit_ans'),
    path('<int:pk>/edit_quest',views.EditQuestion.as_view(),name='edit_quest'),
    path('<int:pk>/edit_subj',views.EditSubject.as_view(),name='edit_subj'),
    path('create_quest/',views.CreateQuestion.as_view(),name='create_question'),
    path('create_ans/',views.CreateAnswer.as_view(),name='create_answer'),
    path('<int:pk>/del_quest',views.DeleteQuestion.as_view(),name='del_quest'),
    path('<int:pk>/del_subj',views.DeleteSubject.as_view(),name='del_subj'),
    path('del_ans/<int:pk>',views.del_ans,name='del_ans'),
    path('search/',views.search,name='search')
]
