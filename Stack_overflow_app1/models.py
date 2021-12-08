from django.db import models

# to work with the tags
from taggit.managers import TaggableManager 
# also include taggit in installed apps else it'll throw error

from django.template.defaultfilters import slugify


# Create your models here.

from django.contrib.auth.models import User # django default User model

class user_profile(models.Model):
    user = models.OneToOneField( User, on_delete = models.CASCADE )
    user_bio = models.CharField(max_length = 200, blank = True)
    
    def __str__(self):
        return self.user.username


# // model for the questions and comments
class Question(models.Model):
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length = 1000)
    slug = models.SlugField(null=True, blank=True)
    created_by = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    # tags = models
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        print(self.slug)
        super().save(*args, **kwargs)


# // commnets and replies handling
class community_comments(models.Model):
    for_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments' )
    comment_body = models.TextField(max_length = 1000)
    comment_by = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add = True)

    # question = models.ForeignKey(Question, on_delete=models.CASCAS)

    is_accepted = models.BooleanField()  # if the answer/comment is accepted

    slug = models.SlugField(null =True, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.for_question)

        super().save(*args, **kwargs)
