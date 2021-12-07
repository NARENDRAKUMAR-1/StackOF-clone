from django.shortcuts import render

# Create your views here.

# let's use django generic views
from django.views.generic import (ListView, DetailView, FormView, CreateView)  # for questions and comments

from . models import user_profile, Question, community_comments
from . forms import community_commentsForm

# import reverse_lazy
from django.urls import reverse_lazy


def welcome(request):

    return render(request, 'welcome.html')

def QuestionListView1(request):
    # questions = Question.objects.all()
    questions= "too many questions"

    return render(request, 'Stack_overflow_app1/questions.html', { 'questions':questions, 'name': "shipmnts" })


class QuestionListView(ListView):
    context_object_name = 'questions'  #many questions
    #  context_object_name  keep this name as it is
    model = Question
    template_name = 'Stack_overflow_app1/questions.html'



class CommunityCommentsView(DetailView):
    context_object_name = 'comments'  #many questions
    #  context_object_name  keep this name as it is
    model = community_comments
    template_name = 'Stack_overflow_app1/question.html'


'''
#  CRUD part
class QuestionCreateView(CreateView):
    form_class =  LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'app2_courses/lesson_create.html'


    # override the default form_valid function of the CreateView class as per our need
    # and store the inputs in our db


    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('app2_courses:lesson_list',
        kwargs={'standard':standard.slug, 'slug':self.object.slug})  # ??
    
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

'''