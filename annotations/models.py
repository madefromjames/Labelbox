from django.db import models

# Create your models here.
class AnnotationProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AnnotationTask(models.Model):
    project = models.ForeignKey(AnnotationProject, on_delete=models.CASCADE, related_name='tasks')
    image_url = models.URLField()
    annotations = models.JSONField(default=dict, blank=True, null=True) # Store annotations as a JSON object
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.project.name } is {self.annotations}"
    