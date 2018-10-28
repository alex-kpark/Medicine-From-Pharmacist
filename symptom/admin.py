from django.contrib import admin
import site

from .models import Patient, Bodypart, Medicine, Logdata


# Filter 구현
class PatientAdmin(admin.ModelAdmin):
    list_filter = ('username',)

    search_fields = ('username', 'email', 'age')

class BodypartAdmin(admin.ModelAdmin):
    list_filter = ('partname',)
    search_fields = ('partname',)

class MedicineAdmin(admin.ModelAdmin):
    list_filter = ('medicinename',)
    search_fields = ('medicinename',)

class LogdataAdmin(admin.ModelAdmin):
    list_filter = ('tmp',)

# Register Modewl
admin.site.register(Patient, PatientAdmin)
admin.site.register(Bodypart, BodypartAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Logdata, LogdataAdmin)