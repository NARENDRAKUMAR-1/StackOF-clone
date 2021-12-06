from django.db import models

# to work with the tags
from taggit.managers import TaggableManager

# Create your models here.

from django.contrib.auth.models import User # django default User model

class user_profie(models.Model):
    user = models.OneToOneField( User, on_delete - CASCADE )
    user_bio = models.CharField(max_length = 200, blank = True)


# // model for the questions and comments
class Question(models.Model):
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length = 1000)
    created_by = models.ForeignKey(user_profile, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    # tags = models
    tags = TaggableManager()


# // commnets and replies handling
class community_comments(models.Model):
    for_question = models.ForeignKey(Question, on_delete=CASCADE )
    comment_body = models.TextField(max_length = 1000)
    comment_by = models.ForeignKey(user_profile, on_delete=CASCADE)
    comment_date = models.DateTimeField(auto_now_add = true)

    is_accepted = models.BooleanField()  # if the answer/comment is accepted
