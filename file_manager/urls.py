from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page par login screen
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Login ke baad is raste par bhejna hai
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('master/clients/', views.manage_clients, name='manage_clients'),
    path('master/folders/', views.all_folders, name='all_folders'),
    path('master/password-reset-requests/', views.master_password_reset_requests, name='master_password_reset_requests'),
    path('master/password-reset-requests/<int:req_id>/reset/', views.master_reset_password, name='master_reset_password'),
    path('master/password-reset-requests/<int:req_id>/informed/', views.master_inform_password_reset, name='master_inform_password_reset'),
    
    path('file/<int:file_id>/', views.file_detail, name='file_detail'),
    path('file/delete/<int:file_id>/', views.delete_shared_file, name='delete_shared_file'),
    path('file/<int:file_id>/save-excel/', views.save_excel, name='save_excel'),
    path('file/<int:file_id>/load-excel/', views.load_excel, name='load_excel'),
    path('password-reset/request/', views.request_password_reset, name='request_password_reset'),
    path('folder/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('folder/edit/<int:folder_id>/', views.edit_folder, name='edit_folder'),
    path('folder/delete/<int:folder_id>/', views.delete_folder, name='delete_folder'),
    # Logout ka rasta
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]