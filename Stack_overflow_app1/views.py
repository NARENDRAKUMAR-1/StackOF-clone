from django.shortcuts import render

# Create your views here.

# let's use django generic views
from django.views.generic import (ListView, DetailView, FormView, CreateView)  # for questions and comments

from . models import user_profile, Question, community_comments
from . forms import community_commentsForm, QuestionForm

# import reverse_lazy
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from Stack_overflow_app1.forms import UserForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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
    context_object_name = 'questions'  #many questions
    #  context_object_name  keep this name as it is
    model = Question
    template_name = 'Stack_overflow_app1/question.html'



# //login logout etc


from Stack_overflow_app1.forms import UserForm

def register(request):
    
    registered = False

    if(request.method=="POST"):
        user_form = UserForm(data = request.POST)
        

        if(user_form.is_valid() ):
            user = user_form.save()
            user.save()

            # // all done
            registered = True

        else:
            print("user_form.errors")
    
    else:
        user_form = UserForm()
        
        #  all these forms are coming from forms.py
        #  forms.py internally uses the models.py in their meta

    
    # //return as
    return render(request,
    'Stack_overflow_app1/register.html',
    {
        'registered' : registered,
        'user_form' : user_form,
        
    })



def user_login(request):

    # '''
    if(request.method == 'POST'):
        username =request.POST.get('username')
        password =request.POST.get('password')

        # //use inbuilt functionality for authentication
        user = authenticate(username = username, password=password)
        # user = authenticate(username = username)

        if user: # authenticated
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('welcome'))
                # index here is namespace for the homepage

            else:
                return HttpResponse("Please Enter correct Credentials or Register Again")

        else:
            return HttpResponse("Username or Password wrong please use the correct credentials")
    
    return render(request, 'Stack_overflow_app1/login.html')
# '''


# login just with the username
'''
    if request.method == 'POST':
            userinput = request.POST['username']

            try:
                username = user_profile.objects.get(user=userinput).username
                return HttpResponseRedirect(reverse('welcome'))
            except user_profile.DoesNotExist:
                username = request.POST['username']
                return HttpResponse("Please Enter correct Credentials or Register Again")

            else:
                return HttpResponse("Please Enter correct Username, can't find the username in records")
            password = request.POST['password']

    
    
    return render(request, 'Stack_overflow_app1/login.html')
'''   

# @login_required #decorator by django
# check if user is logged out
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))







# '''
#  CRUD part
class AnswerCreateView(CreateView):
    form_class =  community_commentsForm
    context_object_name = 'question'
    model = community_comments
    template_name = 'Stack_overflow_app1/question_create.html'


    # override the default form_valid function of the CreateView class as per our need
    # and store the inputs in our db


    def get_success_url(self):
        self.object = self.get_object()
        question = self.object.question
        return reverse_lazy('Stack_overflow_app1:question',
        kwargs={'question':question.slug, 'slug':self.object.slug})  # ??
    
    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        # fm.created_by = self.request.user
        fm.question = self.object.question
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

# '''


