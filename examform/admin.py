from django.contrib import admin
from .models import ExamForm

@admin.register(ExamForm)
class ExamFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'exam_date', 'phone', 'created_at')
    search_fields = ('name', 'course', 'phone')
    list_filter = ('exam_date', 'created_at')
