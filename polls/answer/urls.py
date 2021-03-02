from django.urls import path

from .views import *

urlpatterns = [
    path('', polls_page, name='homepage'),
    path('questions/<int:poll_id>/', questions_page, name='questions'),
    path('choice_answers/<int:question_id>/', choiceanswer_page, name='choice_answer'),
]