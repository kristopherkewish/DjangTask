from django.contrib import admin
from .models import Project, Column, Priority, RequestType, Task, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'created_at']
    search_fields = ['name', 'description']
    list_filter = ['owner', 'created_at']


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ['status', 'created_at']
    search_fields = ['status']


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name', 'score']
    list_editable = ['score']
    ordering = ['-score']


@admin.register(RequestType)
class RequestTypeAdmin(admin.ModelAdmin):
    list_display = ['type']
    search_fields = ['type']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'assignee', 'priority', 'column', 'project', 'due_date', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['priority', 'column', 'project', 'request_type', 'owner', 'assignee', 'created_at']
    filter_horizontal = ['linked_tickets']
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'commenter', 'created_at']
    search_fields = ['comment_text']
    list_filter = ['commenter', 'created_at']
