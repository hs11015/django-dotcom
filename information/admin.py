from django.contrib import admin
from .models import QuestionInformation

# Register your models here.
class QuestionInformationAdmin(admin.ModelAdmin):
    search_fields = ['subject']

#장고 화면사이트에 추가
admin.site.register(QuestionInformation, QuestionInformationAdmin)