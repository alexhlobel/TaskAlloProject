from django.db import models
from django.contrib.auth.models import User


class StatusEmployee(models.Model):
    name = models.TextField(max_length=120)


class Employee(User):
    class Meta:
        abstract = True

    status_emp = models.ForeignKey(StatusEmployee, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=120)


class Worker(Employee):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='worker_team')


class Manager(Employee):
    team = models.ManyToManyField(Team, through='Managership', related_name='manager_team')


class Managership(models.Model):
    team = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='manship_team')
    manager = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='manship_manager')


class Admin(Manager):
    pass


class StatusTask(models.Model):
    name = models.TextField(max_length=120)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.TextField(max_length=120, null=False, blank=False)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='task_team')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Image', null=True, blank=True)
    author = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='task_author')
    status_task = models.ForeignKey(StatusTask, on_delete=models.SET_NULL, null=True, related_name='status_task')
    deadline = models.DateTimeField(null=True, blank=True)
    connection = models.ManyToManyField('Task', null=True, blank=True)

    def __str__(self):
        return self.name
