from django.urls import path
from .views import QuestionListView, QuestionCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('question/create/', QuestionCreateView.as_view(
        template_name='questions/question_create.html'), name='question_create'),
]