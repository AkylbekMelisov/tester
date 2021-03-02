from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Poll, Question, ChoiceAnswer, Answer])
