from django.urls import path
from .views import *
from django import views

urlpatterns = [
    path('homepage/',homepage),
    path('signuppage/',signuppage),
    path('signinpage/',signinpage),
    path('signoutpage/',signoutpage),
    path('create-question/',create_question),
    path('question/<int:pk>/',create_answer_for_a_question,name='question'),
    path('answer/<int:pk>/',like_answer,name='like_answer'),
    
]
