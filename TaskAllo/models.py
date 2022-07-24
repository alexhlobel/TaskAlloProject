from django.db import models
from django.contrib.auth.models import User


class StatusEmployee(models.Model):
    name = models.TextField(max_length=120)

    class Meta:
        verbose_name = 'Status Employee'
        verbose_name_plural = 'Statuses Employee'

    def __str__(self):
        return self.name


class Employee(User):
    class Meta:
        # abstract = True
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    status_emp = models.ForeignKey(StatusEmployee, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Team(models.Model):
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Worker(Employee):
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='worker_team')

    def __str__(self):
        return self.username


class Manager(Employee):
    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    team = models.ManyToManyField(Team, through='Managership', related_name='manager_team')

    def __str__(self):
        return self.username


class Managership(models.Model):
    class Meta:
        verbose_name = 'Managership'
        verbose_name_plural = 'Managerships'

    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='manship_team')
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='manship_manager')

    def __str__(self):
        return f'{self.manager}' + '_' + f'{self.id}'


class Admin(Manager):
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

    pass

    def __str__(self):
        return self.username


class StatusTask(models.Model):
    class Meta:
        verbose_name = 'Status Task'
        verbose_name_plural = 'Status Tasks'

    name = models.TextField(max_length=120)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    name = models.TextField(max_length=120, null=False, blank=False)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='task_team')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # image_source_id = models.OneToOneField(ImageSource, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='task_author')
    status_task = models.ForeignKey(StatusTask, on_delete=models.SET_NULL, null=True, related_name='status_task')
    deadline = models.DateTimeField(null=True, blank=True)
    connection = models.ManyToManyField('Task', null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


class ImageSource(models.Model):
    class Meta:
        verbose_name = 'Image Source'
        verbose_name_plural = 'Image Sources'

    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='source_comment')
    task = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='source_task')


class Image(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    image = models.ImageField(upload_to='Image')
    source = models.ForeignKey(ImageSource, on_delete=models.CASCADE)
