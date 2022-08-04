from apps.Employees.models import *
from apps.Comments.models import Comment
from django.contrib.auth.models import AbstractUser


class ImageTask(models.Model):
    image_task = models.ImageField(upload_to='Image')


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
    creator = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, max_length=15,
                                   limit_choices_to={'role': (RolesChoice.manager, RolesChoice.admin)})
    status_task = models.TextField(choices=StatusTaskChoice.choices, default='Backlog', verbose_name='Status task')
    deadline = models.DateTimeField(null=True, blank=True)
    image_task = models.ManyToManyField(ImageTask)
    assigned_task = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='assigned_task')
    comment_task = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, related_name='Comment')

    def __str__(self):
        return self.name
