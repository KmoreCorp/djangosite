from django.contrib import admin

# Register your models here.
from poll.models import Subject, Teacher

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'create_date', 'is_hot')
    ordering =('no',)
    search_fields =('name', )

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'detail', 'good_count', 'bad_count', 'subject')
    search_fields = ('name', 'subject')

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)