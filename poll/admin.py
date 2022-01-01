from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceAdmin(admin.StackedInline):
    model =Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ['poll','question','type']
    inlines = [ChoiceAdmin]
class question(admin.StackedInline):
    model = Question

class PollsAdmin(admin.ModelAdmin):
    fields = ['title','end_date','description']
    inlines = [question]



admin.site.register(Poll, PollsAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(ResultsModel)