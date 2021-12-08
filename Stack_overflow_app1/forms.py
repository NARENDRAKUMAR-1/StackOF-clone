from django import forms

from . models import community_comments, Question

class community_commentsForm(forms.ModelForm):
    class Meta:
        model = community_comments
        fields = ('comment_body', 'is_accepted')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'body', 'tags')


from django.contrib.auth.forms import UserCreationForm
from Stack_overflow_app1.models import user_profile
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name')

        # widgets = {
        # "password":"forms.PasswordInput()",
        # }

        # labels = {
        # 'password1':'Password',
        # 'password2':'Confirm Password'
        # }