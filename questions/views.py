from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView)
from .models import Question
# Create your views here.
# This is the view for index/home page of education hub


class QuestionListView(ListView):
    '''
    List View for Question Template
    '''
    model = Question
    template_name = 'index.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']


class QuestionCreateView(LoginRequiredMixin, CreateView):
    '''
    Create View for Question model
    '''
    model = Question
    fields = ['title', 'description']

    # Setting the author befor the question is posted

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionDetailView(DetailView):
    '''
    Detail View for a single question
    '''
    model = Question


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Update View for Question model
    '''
    model = Question
    fields = ['title', 'description']

    # Setting the author befor the question is posted

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Testing if the user if the one who created the post

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/'
    # Testing if the user if the one who created the post

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
