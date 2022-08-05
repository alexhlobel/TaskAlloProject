from apps.Employees.models import CustomUser, Team, RolesChoice, StatusWorkerChoice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


class ImageTask(models.Model):
    image_task = models.ImageField(upload_to='Image')
    source_task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='source_task', null=True, blank=True)


class StatusTaskChoice(models.TextChoices):
    backlog = 'Backlog'
    ready_to_dev = 'Ready to dev'
    in_progress = 'In progress'
    ready_to_qa = 'Ready to QA'
    production = 'Production'


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    name = models.TextField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='task_team', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                                limit_choices_to=Q(role=RolesChoice.admin) | Q(role=RolesChoice.manager))
    Q(share_holder=True) | Q(distributor=True)
    status_task = models.TextField(choices=StatusTaskChoice.choices, default='Backlog', verbose_name='Status task')
    deadline = models.DateTimeField(null=True, blank=True)
    # image_task = models.ManyToManyField(ImageTask)

    def __str__(self):
        return self.name
