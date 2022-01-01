from django.urls import path, include
from .views import *
urlpatterns = [
    path('',polls, name='polls'),
    path('poll/<int:poll_id>/',show_poll, name='poll'),
    path('question/<int:question_id>',show_question, name='question'),
    path('login', login.as_view())
]
