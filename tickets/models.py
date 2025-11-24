from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Column(models.Model):
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['created_at']


class Priority(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-score']
        verbose_name_plural = 'Priorities'


class RequestType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_tasks')
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateTimeField(null=True, blank=True)
    request_type = models.ForeignKey(RequestType, on_delete=models.PROTECT)
    linked_tickets = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='linked_to')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.task.title}"

    class Meta:
        ordering = ['created_at']