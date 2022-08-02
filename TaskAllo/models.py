from django.db import models
from django.contrib.auth.models import AbstractUser


class RolesChoice(models.TextChoices):
    worker = 'worker'
    manager = 'manager'
    admin = 'admin'
    hard = 'hard'


class StatusWorkerChoice(models.TextChoices):
    In_team = 'In_team'
    Bench = 'Bench'


class CustomUser(AbstractUser):
    role = models.CharField(choices=RolesChoice.choices, max_length=20)


class ImageTask(models.Model):
    image_task = models.ImageField(upload_to='Image')


class ImageComment(models.Model):
    image_comment = models.ImageField(upload_to='Image')


class Team(models.Model):
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    name = models.CharField(max_length=150)
    worker = models.OneToOneField(CustomUser, on_delete=models.Prefetch, limit_choices_to={'role': RolesChoice.worker},
                                  related_name='worker')
    manager = models.ManyToManyField(CustomUser, limit_choices_to={"role": RolesChoice.manager}, related_name='manager')

    def __str__(self):
        return self.name


class StatusTaskChoice(models.TextChoices):
    Backlog = 'Backlog'
    Ready_to_dev = 'Ready to dev'
    In_progress = 'In progress'
    Ready_to_QA = 'Ready to QA'
    Production = 'Production'


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image_comment = models.ManyToManyField(ImageComment, blank=True)

    def __str__(self):
        return self.content[:50]


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    name = models.TextField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='task_team', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False,
                               related_name='task_author')
    status_task = models.TextField(choices=StatusTaskChoice.choices, default='Backlog', verbose_name='Status task')
    deadline = models.DateTimeField(null=True, blank=True)
    image_task = models.ManyToManyField(ImageTask, blank=True)
    comment_task = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, related_name='Comment')

    def __str__(self):
        return self.name

# class Employee(User):
#     emp_status = [
#         ('in team', 'In team'),
#         ('bench', 'Bench'),
#         ('fired', 'Fired')
#     ]
#
#     class Meta:
#         # abstract = True
#         verbose_name = 'Employee'
#         verbose_name_plural = 'Employees'
#
#     status_emp = models.TextField(max_length=120, choices=emp_status, verbose_name='Status Employee')
#
#     def __str__(self):
#         return self.username
#
#
# class Team(models.Model):
#     class Meta:
#         verbose_name = 'Team'
#         verbose_name_plural = 'Teams'
#
#     name = models.CharField(max_length=120)
#
#     def __str__(self):
#         return self.name
#
#
# class Worker(Employee):
#     class Meta:
#         verbose_name = 'Worker'
#         verbose_name_plural = 'Workers'
#
#     team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_team')
#
#     def __str__(self):
#         return self.username
#
#
# class Manager(Employee):
#     class Meta:
#         verbose_name = 'Manager'
#         verbose_name_plural = 'Managers'
#
#     team = models.ManyToManyField(Team, through='Managership', related_name='manager_team')
#
#     def __str__(self):
#         return self.username
#
#
# class Managership(models.Model):
#     class Meta:
#         verbose_name = 'Managership'
#         verbose_name_plural = 'Managerships'
#
#     team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='manship_team')
#     manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True,
#                                 related_name='manship_manager')
#
#     def __str__(self):
#         return f'{self.manager}' + '_' + f'{self.id}'
#
#
# class Admin(Manager):
#     class Meta:
#         verbose_name = 'Admin'
#         verbose_name_plural = 'Admins'
#
#     pass
#
#     def __str__(self):
#         return self.username
#
#
# class ImageSource(models.Model):
#     class Meta:
#         verbose_name = 'Image Source'
#         verbose_name_plural = 'Image Sources'
#
#     pass
#
#     def __str__(self):
#         return 'Source ' + f'{self.id}'
#
#
# class Task(models.Model):
#     name_status = [
#         ('backlog', 'Backlog'),
#         ('ready to dev', 'Ready to Dev'),
#         ('in progress', 'In progress'),
#         ('ready to QA', 'Ready to QA'),
#         ('production', 'Production')
#     ]
#
#     class Meta:
#         verbose_name = 'Task'
#         verbose_name_plural = 'Tasks'
#
#     name = models.TextField(max_length=120, null=False, blank=False)
#     description = models.TextField()
#     team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='task_team')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     image_source = models.OneToOneField(ImageSource, on_delete=models.CASCADE, null=True, blank=True)
#     author = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='task_author')
#     status_task = models.TextField(max_length=120, choices=name_status, default='Backlog', verbose_name='Status task')
#     deadline = models.DateTimeField(null=True, blank=True)
#     connection = models.ManyToManyField('Task', null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Connection(models.Model):
#     class Meta:
#         verbose_name = 'Connection'
#         verbose_name_plural = 'Connections'
#
#     task_1 = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True,
#                                related_name='task_1')
#     task_2 = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True,
#                                related_name='task_2')
#
#     def __str__(self):
#         return f'{self.task_1}' + ' - ' + f'{self.task_2}'
#
#
# class Comment(models.Model):
#     class Meta:
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'
#
#     owner = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     content = models.TextField()
#     image_source = models.OneToOneField(ImageSource, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return self.content[:50]
#
#
# class Image(models.Model):
#     class Meta:
#         verbose_name = 'Image'
#         verbose_name_plural = 'Images'
#
#     image = models.ImageField(upload_to='Image')
#     source = models.ForeignKey(ImageSource, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.image.name
