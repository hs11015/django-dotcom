from django.contrib import admin
from .models import QuestionMinor

# Register your models here.
class QuestionMinorAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#장고 화면사이트에 추가
admin.site.register(QuestionMinor, QuestionMinorAdmin)