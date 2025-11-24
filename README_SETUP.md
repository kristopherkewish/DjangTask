# DjangTask - Project Management System

A Django-based task management system with kanban board functionality.

## Features Implemented (MVP)

### User Authentication
- ✅ Login/Logout
- ✅ Password reset functionality
- ✅ User-specific project views

### Projects
- ✅ Create new projects
- ✅ Edit project details (name, description)
- ✅ Archive projects
- ✅ List all active projects
- ✅ Owner-only permissions

### Kanban Board
- ✅ 3 default columns (Backlog, In Progress, Done)
- ✅ Visual board layout with Bootstrap styling
- ✅ Task counts per column

### Tasks
- ✅ Create tasks in any column
- ✅ Edit task details (title, description, priority, due date)
- ✅ Move tasks between columns
- ✅ View task details
- ✅ Assign tasks to users
- ✅ Task types (Bug, Feature, Enhancement, etc.)
- ✅ Priority levels (Critical, High, Medium, Low)

### Comments
- ✅ Add comments to tasks
- ✅ View all comments with timestamps
- ✅ Comment author tracking

## Setup Instructions

### 1. Activate Virtual Environment
```bash
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Initial Data (Columns, Priorities, Request Types)
```bash
python manage.py setup_initial_data
```

### 4. Create a Superuser
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
- Main app: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## Usage

1. **Login**: Use the superuser credentials you created
2. **Create a Project**: Click "Create New Project" from the projects list
3. **View Board**: Click on a project to see the kanban board
4. **Create Tasks**: Click "Create Task" and fill in the details
5. **Move Tasks**: Click on a task to view details, then use "Move" to change columns
6. **Add Comments**: From the task detail page, add comments to discuss the task

## File Structure

```
tickets/
├── models.py                 # Data models (Project, Task, Comment, etc.)
├── views.py                  # View functions for all pages
├── forms.py                  # Django forms for user input
├── urls.py                   # URL routing
├── admin.py                  # Admin panel configuration
├── templates/tickets/        # HTML templates
│   ├── base.html            # Base template with navbar
│   ├── home.html            # Landing page
│   ├── login.html           # Login page
│   ├── project_list.html    # List of projects
│   ├── project_board.html   # Kanban board view
│   ├── task_detail.html     # Task details with comments
│   └── ...
├── templatetags/            # Custom template filters
│   └── ticket_filters.py    # Filters for dict access and priority colors
└── management/commands/      # Custom management commands
    └── setup_initial_data.py # Initialize default data
```

## Models

- **Project**: User's projects with name, description, and archive status
- **Column**: Board columns (Backlog, In Progress, Done)
- **Task**: Tasks with title, description, priority, due date, etc.
- **Comment**: Comments on tasks
- **Priority**: Priority levels with scores
- **RequestType**: Types of requests (Bug, Feature, etc.)

## Notes

- All mutations (create, edit, delete) are done through custom views, not Django admin
- Django admin is available for superuser management and debugging
- Bootstrap 5 is used for styling (loaded via CDN)
- PostgreSQL database configuration is in settings.py
