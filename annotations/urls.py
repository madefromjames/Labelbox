from django.urls import path
from annotations.views import index, annotation_screen, save_annotation

urlpatterns = [
    path('', index, name='index'),
    path('annotate/<int:task_id>/', annotation_screen, name='annotation_screen'),
    path('save_annotation/<int:task_id>/', save_annotation, name='save_annotation'),
]