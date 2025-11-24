from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Project, Task, Comment, Column
from .forms import ProjectForm, TaskForm, CommentForm, TaskMoveForm


def home(request):
    if request.user.is_authenticated:
        return redirect('project_list')
    return render(request, 'tickets/home.html')


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user, is_archived=False)
    return render(request, 'tickets/project_list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, f'Project "{project.name}" created successfully!')
            return redirect('project_board', project_id=project.id)
    else:
        form = ProjectForm()
    return render(request, 'tickets/project_form.html', {'form': form, 'action': 'Create'})


@login_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Project "{project.name}" updated successfully!')
            return redirect('project_board', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'tickets/project_form.html', {'form': form, 'action': 'Edit', 'project': project})


@login_required
def project_archive(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        project.is_archived = True
        project.save()
        messages.success(request, f'Project "{project.name}" archived successfully!')
        return redirect('project_list')
    return render(request, 'tickets/project_confirm_archive.html', {'project': project})


@login_required
def project_board(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    columns = Column.objects.all()
    tasks_by_column = {}
    for column in columns:
        tasks_by_column[column] = project.tasks.filter(column=column)
    return render(request, 'tickets/project_board.html', {
        'project': project,
        'columns': columns,
        'tasks_by_column': tasks_by_column
    })


@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.project = project
            task.save()
            messages.success(request, f'Task "{task.title}" created successfully!')
            return redirect('project_board', project_id=project.id)
    else:
        form = TaskForm(project=project)
    return render(request, 'tickets/task_form.html', {'form': form, 'project': project, 'action': 'Create'})


@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project=task.project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Task "{task.title}" updated successfully!')
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task, project=task.project)
    return render(request, 'tickets/task_form.html', {'form': form, 'project': task.project, 'action': 'Edit', 'task': task})


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    comments = task.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.commenter = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('task_detail', task_id=task.id)
    else:
        comment_form = CommentForm()
    
    return render(request, 'tickets/task_detail.html', {
        'task': task,
        'comments': comments,
        'comment_form': comment_form
    })


@login_required
def task_move(request, task_id):
    task = get_object_or_404(Task, id=task_id, project__owner=request.user)
    if request.method == 'POST':
        form = TaskMoveForm(request.POST)
        if form.is_valid():
            task.column = form.cleaned_data['column']
            task.save()
            messages.success(request, f'Task moved to "{task.column.status}"!')
            return redirect('project_board', project_id=task.project.id)
    else:
        form = TaskMoveForm(initial={'column': task.column})
    return render(request, 'tickets/task_move.html', {'form': form, 'task': task})