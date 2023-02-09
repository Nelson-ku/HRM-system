from django.urls import path

from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('payL',views.Pay,name='payL'),
    path('employee_form/', views.createEmployee, name="employee_form"),
    path('modules_form/', views.Modules_files, name="modules_form"),
    path('healthform/',views.Health_info,name="healthform"),
    path('healthinfo/',views.Healthfiles,name="healthinfo"),
    path('modules_update/<str:pk>/',views.ModulesUpdate, name='modules_update'),
    path('modules_delete/<str:pk>/',views.Modules_delete, name='modules_delete'),
    path('modules_copy/', views.modules_copy, name="modules_copy"),

    path('Docs/', views.Documentation, name="Docs"),
    path('task/', views.Task, name="task_form"),
    path('update_task/<str:pk>/', views.updateTask, name='update_tasks'),
    path('delete_tasks/<str:pk>/', views.deleteTask, name='delete_tasks'),
    path('completed_tasks/', views.Completed_tasks, name="completed_tasks"),
    path('pending_tasks/', views.Pending_tasks, name="pending_tasks"),
    path('rejected_tasks/', views.Rejected_tasks, name="rejected_tasks"),
    path('completed_tasks/', views.Completed_tasks, name="completed_tasks"),
    path('tasks_allocated/', views.Total_tasks, name="tasks_allocated"),
    path('work_request', views.workApproval, name="work_request"),
    path('work_request_list', views.workRequests, name="work_request_list"),

    path('',views.index,name='index'),

    path('supervisors/', views.Supervisors, name="supervisors"),

    path('account_settings/',views.accountSettings,name="account_settings"),
    path('user/', views.userPage, name="user-page"),
    path('user-pending/', views.userPending, name="user-pending"),
    path('user-completed/', views.userCompleted, name="user-completed"),
    path('user-rejected/', views.userRejected, name="user-rejected"),
    path('userpay/', views.userPayroll, name="userpay"),

    path('employees/',views.employees,name="employees"),
    path('employees_pdf/', views.Employee_pdf, name="employees_pdf"),
    path('tasks_pdf/', views.Task_pdf, name="tasks_pdf"),
    path('Completed-tasks_pdf/', views.CompletedTask_pdf, name="Completed-tasks_pdf"),
    path('pending-tasks_pdf/', views.PendingTask_pdf, name="Pending-tasks_pdf"),
    path('rejected-tasks_pdf/', views.RejectedTask_pdf, name="Rejected-tasks_pdf"),

    path('Asset_list/', views.Asset_list, name="Asset_list"),
    path('Asset/', views.Allocate_asset, name="Asset"),
    path('userAsset/', views.user_asset_list, name="userAsset"),
    path('assets_pdf/', views.Asset_pdf, name="assets_pdf"),


    path('status/',views.status,name='status'),
    path('update_employee/<str:pk>/',views.updateEmployee, name='update_employee'),
    path('delete_employee/<str:pk>/',views.deleteEmployee, name='delete_employee'),

    path('leave/',views.Leave_alloctaion, name='leave'),
    path('allocated_leave/', views.Leavelist, name='allocated_leave'),




#reset password using email
    #1 submits email form
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html" ),
         name="reset_password"),
    #2 email sent success message
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
     #3 link to password Reset form in Email
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
      #password succesfully changed
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
]