# Concrete Feature List (MVP First)

## MVP (this alone is enough to show off)

### Entities

- **User** (Django's built-in)
- **Project**
- **Column** (e.g. "Backlog", "In Progress", "Done")
- **Task**
- **Comment** (on Task)

### Core Features

#### User Auth

- Sign up, login, logout, password reset (Django auth views)

#### Projects

- List of your projects
- Create / rename / archive project

#### Columns

- Default 3 columns created for each new project
- Optional: ability to add/reorder columns

#### Tasks

- Create task in a column
- Edit title & description
- Move task between columns (simple dropdown or basic JS, doesn't have to be fancy drag-and-drop)
- Optional: assign due date and priority

#### Comments

- Add comments per task
- Show who commented & when

#### Permissions

- Only owner sees a project (for MVP; collaboration can be stretch)

#### Basic UI

- Project board view: columns + tasks in a simple grid
- Navigation bar with "My Projects", "Profile", "Logout"

**That's a solid, non-toy app already.**

---

## Stretch Features (if you have time)

Pick some, not all:

### 👥 Collaborators

- `ProjectMember` model with role (owner, editor, viewer)
- Invite by email (simple: type email, if user exists, add them)

### 🔍 Search & Filters

- Filter tasks by text, status, or due date

### 📊 Dashboard

- Simple stats per project (e.g. task counts per column, tasks due this week)

### 🧵 Activity Log Log

- Model to track "User X moved Task Y from A to B"

### 🌐 REST API

- Small set of endpoints with Django REST Framework for tasks/projects

### 🎨 Better UX

- Drag-and-drop tasks between columns with minimal JS
- Toast messages for success/errors

**Each one of these is portfolio candy.**
