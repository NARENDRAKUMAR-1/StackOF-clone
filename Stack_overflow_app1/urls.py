from django.urls import path

from . import views

app_name = 'Stack_overflow_app1' #declare the app_name here it's must

urlpatterns = [
    # path('', views.welcome, name ="welcome"),

    # path('q/', views.QuestionListView1, name ='question_list1' )

    # path('<str:question>/<slug:slug>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('', views.QuestionListView.as_view(), name='question_list'),

    path('/<slug:slug>/', views.CommunityCommentsView.as_view(), name='comments'),


    path('register/', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),


    # path('<str:question>/<str:slug>/create/', views.AnswerCreateView.as_view(), name='question_create'),
    path('<str:slug>/create/', views.AnswerCreateView.as_view(), name='question_create'),



]


