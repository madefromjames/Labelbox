from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import AnnotationTask
import json

def annotation_screen(request, task_id):
    """
    Renders the annotation screen for a given task.
    """
    task = get_object_or_404(AnnotationTask, id=task_id)
    return render(request, 'annotations/annotation_screen.html', {'task': task})

def save_annotation(request, task_id):
    """
    Saves annotations for a given task.
    """
    task = get_object_or_404(AnnotationTask, id=task_id)
    if request.method == 'POST':
        annotations = request.POST.get('annotation', '{}')
        try:
            task.annotations = json.loads(annotations)
            task.save()
            messages.success(request, "Annotation saved successfully!")
        except json.JSONDecodeError:
            messages.error(request, "Invalid JSON format")
        return redirect('annotation_screen', task_id=task.id)
    return render(request, 'annotations/annotation_screen.html', {'task': task})
