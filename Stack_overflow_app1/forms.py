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