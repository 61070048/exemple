from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)