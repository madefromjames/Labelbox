from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import AnnotationTask
import json

# Create your views here.
def annotation_screen(request, task_id):
    task = get_object_or_404(AnnotationTask, id=task_id)
    return render(request, 'annotations/annotation_screen.html', {'task': task})

def save_annotation(request, task_id):
    if request.method == 'POST':
        try:
            task = get_object_or_404(AnnotationTask, id=task_id)
            data = json.loads(request.body)
            task.annotations = data
            task.save()
            return JsonResponse({'status': "success", 'message': "Annotation saved successfully"})
        except task.annotations.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found'})