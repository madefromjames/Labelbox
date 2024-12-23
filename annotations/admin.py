from django.contrib import admin
from .models import AnnotationProject, AnnotationTask

# Register your models here.
class AnnotationProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class AnnotationTaskAdmin(admin.ModelAdmin):
    list_display = ('project', 'image_url', 'annotations', 'created_at')
    search_fields = ('project__name', 'image_url')

admin.site.register(AnnotationProject, AnnotationProjectAdmin)
admin.site.register(AnnotationTask, AnnotationTaskAdmin)