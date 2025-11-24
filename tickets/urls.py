from django.urls import path
from django.contrib.auth import views as auth_views
from tickets import views


urlpatterns = [
    path("", views.home, name="home"),
    
    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='tickets/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', auth_views.LoginView.as_view(template_name='tickets/signup.html'), name='signup'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='tickets/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='tickets/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tickets/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='tickets/password_reset_complete.html'), name='password_reset_complete'),
    
    # Project URLs
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/', views.project_board, name='project_board'),
    path('projects/<int:project_id>/edit/', views.project_edit, name='project_edit'),
    path('projects/<int:project_id>/archive/', views.project_archive, name='project_archive'),
    
    # Task URLs
    path('projects/<int:project_id>/tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/move/', views.task_move, name='task_move'),
]
