from django.contrib import admin

# Register your models here.

from .models import user_profile, Question, community_comments

admin.site.register(user_profile)
admin.site.register(Question)
admin.site.register(community_comments)
