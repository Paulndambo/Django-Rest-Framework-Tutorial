from time import timezone
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

"""
@receiver(post_save, sender=Task)
@receiver(post_delete, sender=Task)
def update_project_last_modified(sender, instance, **kwargs):
    instance.project.last_modified = timezone.now()
    instance.project.save()
"""

