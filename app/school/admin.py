from django.contrib import admin

from .models import School, Student

class SchoolAdmin(admin.ModelAdmin):
    pass
admin.site.register(School, SchoolAdmin)


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)
