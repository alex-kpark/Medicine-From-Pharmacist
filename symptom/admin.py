from django.contrib import admin
import site

from .models import Patient, Questions


# Filter 구현
class PatientAdmin(admin.ModelAdmin):
    list_filter = ('nickname',)

    search_fields = ('nickname', 'email', 'age')

class QuestionsAdmin(admin.ModelAdmin):
    list_filter = ('question_a',)

# Register Modewl
admin.site.register(Patient, PatientAdmin)
admin.site.register(Questions, QuestionsAdmin)
