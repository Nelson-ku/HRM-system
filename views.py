from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import  CreateUserForm, CustomerForm, EmployeeForm, HealthForm, ModulesForm, TaskForm, \
     LeaveForm,AssetForm,WorkapprovalForm
from .filters import TaskFilter
from django.contrib import messages
from .decorators import  unauthenticated_user,allowed_users, admin_only
from datetime import datetime, date
from django.db.models import Sum

#report
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

x = datetime.now()
y = x.strftime('%m/%d/%y')
date = date.today()




#generate a pdf employe list
@admin_only
@login_required(login_url='login')
def Employee_pdf(request):

    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica',14)

    employees = Employee.objects.all()

    lines =[]
    lines.append('LAKE GROUP COMPANY LIMITED')
    lines.append('Available employees available ')
    lines.append("This report was generated on " + str(date))

    for employee in employees:
        lines.append(" ")
        lines.append("PHONE:  " + employee.id)
        lines.append("FIRST NAME: "+ employee.middle_name)
        lines.append("MIDDLE NAME: "+ employee.last_name)
        lines.append("EMAIL:  " + employee.email)

        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True ,filename='employees.pdf')

@admin_only
@login_required(login_url='login')
def Asset_pdf(request):

    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica',14)

    assets = Assets.objects.all()

    lines =[]
    lines.append('LAKE GROUP COMPANY LIMITED')
    lines.append('All employees assets records')
    lines.append("This report was generated on " + str(date))

    for Asset in assets:

        lines.append(' ')
        lines.append("Name :"+ Asset.customer.name)
        lines.append("Employee id :" + Asset.asset_allocated)
        lines.append("Task id :" + str(Asset.asset_id))
        lines.append("condition:" + Asset.condition)


        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True ,filename='assets.pdf')

@admin_only
@login_required(login_url='login')
def Task_pdf(request):


    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica',14)

    tasks = Tasks.objects.all()

    lines =[]
    lines.append('LAKE GROUP COMPANY LIMITED ')

    lines.append('All assigned Tasks')

    lines.append("This report was generated on " + str(date))


    for task in tasks:
        lines.append(" ")
        lines.append(" Employee Name : "+ task.customer.name)
        lines.append(" Employee id : " + str(task.customer.id))
        lines.append("Task assigned: " + task.weekly_task)
        lines.append("date_assigned " + str(task.date_created.strftime('%d,%m,%y')))
        lines.append("Task id: " + str(task.id))
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True ,filename='task.pdf')

@admin_only
@login_required(login_url='login')
def CompletedTask_pdf(request):

    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica',14)

    tasks = Tasks.objects.all()
    completed = tasks.filter(status='completed')

    lines =[]
    lines.append('LAKE GROUP COMPANY LIMITED')
    lines.append('All completed Tasks')
    lines.append("This report was generated on " + str(date))


    for task in completed:
        lines.append(" ")
        lines.append("Name :"+ task.customer.name)
        lines.append("Employee id:" + str(task.customer.id))
        lines.append("Task assigned: " + task.weekly_task)
        lines.append("date_assigned " + str(task.date_created.strftime('%d,%m,%y')))
        lines.append("Task id: " + str(task.id))
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True ,filename='completed-tasks.pdf')
@admin_only
@login_required(login_url='login')
def PendingTask_pdf(request):

    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica',14)

    tasks = Tasks.objects.all()
    pending = tasks.filter(status='pending')

    lines =[]
    lines.append('LAKE GROUP COMPANY LIMITED')
    lines.append('All pending tasks')
    lines.append("This report was generated on  " + str(date))

    for task in pending:
        lines.append(" ")
        lines.append("Name :"+ task.employee.first_name)
        lines.append("Employee id:" + str(task.employee.id))
        lines.append("Task assigned:" + task.weekly_task)
        lines.append(" Task id :" + str(task.id))
        lines.append(" date_assigned :" + str(task.date_created.strftime('%d,%m,%y')))


        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True ,filename='pending-tasks.pdf')

@admin_only
@login_required(login_url='login')
def RejectedTask_pdf(request):

    buf=io.BytesIO()

    c=canvas.Canvas(buf,pagesize=letter, bottomup=0)

    textob=c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica',14)

    tasks = Tasks.objects.all()
    rejected = tasks.filter(status='rejected')

    lines =[]
    lines.append('LAKE GROUP COMPANY LIMITED')
    lines.append('All rejected tasks')
    lines.append("This report was generated on " + str(date))




    for task in rejected:
        lines.append(" ")
        lines.append("Name :" + task.employee.first_name)
        lines.append(" Employee_id:" + str(task.employee.id))
        lines.append("Task id :" + str(task.id))
        lines.append("Task assigned:" + task.weekly_task)
        lines.append("date_assigned" + str(task.date_created.strftime('%d,%m,%y')))
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True ,filename='rejected-tasks.pdf')
# Create your views here.


@admin_only
@login_required(login_url='login')
def Allocate_asset(request):
    form = AssetForm()
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'accounts/allocate_assets.html', context)


@login_required(login_url='login')
def workApproval(request):
    form = WorkapprovalForm()
    if request.method == 'POST':
        form = WorkapprovalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'accounts/approval.html', context)


@login_required(login_url='login')
def workRequests(request):
    works=work_approval_request.objects.all()

    context={'works':works}
    return render(request, 'accounts/task_approval_list.html',context)


@admin_only
@login_required(login_url='login')
def Asset_list(request):
    assets = Assets.objects.all()

    context = {'assets': assets}
    return render(request, 'accounts/Asset_list.html', context)


@login_required(login_url='login')
def user_asset_list(request):
    c_assets = request.user.customer.assets_set.all()

    context = {'c_assets': c_assets}
    return render(request, 'accounts/user_asset.html', context)



@admin_only
@login_required(login_url='login')
def Modules_files(request):
    if request.method == 'POST':
        form = ModulesForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.is_valid())
            form.save()
        return redirect('index')
    else:
        form = ModulesForm()
    context = {'form': form}
    return render(request, 'accounts/modules_form.html', context)

@login_required(login_url='login')
@admin_only
def Salary(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        form = NetsalaryForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('index')
    else:
        form = NetsalaryForm()
    context = {'form': form, 'employees': employees}
    return render(request, 'accounts/NetSalary.html', context)

@login_required(login_url='login')
def Health_info(request):
    if request.method == 'POST':
        form = HealthForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.is_valid())
            form.save()
        return redirect('healthinfo')
    else:
        form = HealthForm()
    context = {'form': form}

    return render(request, 'accounts/healthform.html', context)

@login_required(login_url='login')
def Healthfiles(request):
    healthinfo = Healthinfo.objects.all()
    context = {'healthinfo': healthinfo}

    return render(request, 'accounts/Health_record.html', context)
@admin_only
@login_required(login_url='login')
def ModulesUpdate(request, pk):
    modules = Modules.objects.get(id=pk)
    form = ModulesForm(instance=modules)

    if request.method == 'POST':
        # print('printing post', request.POST)
        form = ModulesForm(request.POST, request.FILES, instance=modules)
        if form.is_valid():
            form.save()
            return redirect('modules_copy')

    context = {'form': form}
    return render(request, 'accounts/modules_form.html', context)
@admin_only
@login_required(login_url='login')
def Modules_delete(request, pk):
    modules = Modules.objects.get(id=pk)
    if request.method == 'POST':
        form = ModulesForm(request.POST, request.FILES, instance=modules)
        if form.is_valid():
            modules.delete()
            return redirect('modules_copy')

    context = {'modules': modules}
    return render(request, 'accounts/modules_delete.html', context)


@login_required(login_url='login')
@admin_only
def Task(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('employees')

    context = {'form': form, "tasks":tasks}
    return render(request, 'accounts/tasks.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['supervisors'])
def updateTask(request, pk):
    tasks = Tasks.objects.get(id=pk)
    form = TaskForm(instance=tasks)

    if request.method == 'POST':
        # print('printing post', request.POST)
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('tasks_allocated')

    context = {'form': form}
    return render(request, 'accounts/tasks.html', context)
@admin_only
@login_required(login_url='login')
def deleteTask(request, pk):
    tasks = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('tasks_allocated')

    context = {'tasks': tasks}
    return render(request, 'accounts/delete_tasks.html', context)

@login_required(login_url='login')
def Total_tasks(request):

    tasks = Tasks.objects.all()
    myFilter=TaskFilter(request.GET,queryset=tasks)
    tasks=myFilter.qs

    context = {'tasks': tasks,'myFilter':myFilter}
    return render(request, 'accounts/Tasks_allocated.html', context)

#generate a pdf task list


@login_required(login_url='login')
def Completed_tasks(request):
    tasks = Tasks.objects.all()
    completed = tasks.filter(status='completed')
    AtFilter=TaskFilter(request.GET, queryset=completed)
    completed=AtFilter.qs

    context = {'completed': completed, 'AtFilter':AtFilter}
    return render(request, 'accounts/completed_tasks.html', context)

@login_required(login_url='login')
def Pending_tasks(request):
    tasks = Tasks.objects.all()
    pending = tasks.filter(status='pending')

    context = {'pending': pending}
    return render(request, 'accounts/pending_tasks.html', context)

@login_required(login_url='login')
def Rejected_tasks(request):
    tasks = Tasks.objects.all()
    rejected = tasks.filter(status='rejected')

    context = {'rejected': rejected}
    return render(request, 'accounts/rejected_tasks.html', context)

@login_required(login_url='login')
def modules_copy(request):
    moduless = Modules.objects.all()

    context = {'moduless': moduless}
    return render(request, 'accounts/modules_copy.html', context)


@admin_only
@login_required(login_url='login')
def Leave_alloctaion(request,):
    form = LeaveForm()

    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
        else:
                pass

    context = {'form': form}
    return render(request, 'accounts/leave_form.html', context)

@login_required(login_url='login')
def Documentation(request):
    return render(request, 'accounts/Documentation.html')


@login_required(login_url='login')
def Leavelist(request):

    leaves = Leave.objects.all()

    context = {'leaves': leaves}
    return render(request, 'accounts/allocated_leave.html', context)



@login_required(login_url='login')
def Pay(request):
    employees = Employee.objects.all()
    total= Employee.objects.aggregate(Total=Sum('salary'))
    print(total)
    context = {'employees': employees, 'total':total}
    return render(request, 'accounts/pay.html', context)



@login_required(login_url='login')
@admin_only
def employees(request):
    employees = Employee.objects.all()

    context = {'employees': employees}
    return render(request, 'accounts/Employees.html', context)

@admin_only
@login_required(login_url='login')
def createEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm()
    context = {'form': form}
    return render(request, 'accounts/Employee_form.html', context)

@admin_only
@login_required(login_url='login')
def updateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        # print('printing post', request.POST)
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')

    context = {'form': form}
    return render(request, 'accounts/Employee_form.html', context)
@admin_only
@login_required(login_url='login')
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employees')

    context = {'employee': employee}
    return render(request, 'accounts/delete_employee.html', context)


# @unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# @unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)

    return redirect('login')


@login_required(login_url='login')
@csrf_exempt
@admin_only
def index(request):

    assets=Assets.objects.all()
    tasks = Tasks.objects.filter(date_created=date.today())
    myFilter=TaskFilter(request.GET,queryset=tasks)
    tasks=myFilter.qs
    assets_total=assets.count()

    customers = Customer.objects.all()
    employees = Employee.objects.all()
    total_tasks = tasks.count()
    total_employees = employees.count()

    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status='pending').count()
    rejected_tasks = tasks.filter(status='rejected').count()

    total_registered_employees = customers.count()
    context = {'total_registered_employees':total_registered_employees,'customers':
        customers,'tasks':tasks, 'total_employees': total_employees, "rejected_tasks": rejected_tasks,
        "completed_tasks": completed_tasks, "pending_tasks": pending_tasks,
               "total_tasks": total_tasks,  'date': y , 'assets_total':assets_total,'myFilter':myFilter}

    return render(request, 'accounts/index.html', context)

@login_required(login_url='login')
@csrf_exempt
@allowed_users(allowed_roles=['supervisors'])
def Supervisors(request):
    tasks = Tasks.objects.filter(date_created=date.today())
    myFilter=TaskFilter(request.GET,queryset=tasks)
    tasks=myFilter.qs
    customers = Customer.objects.all()
    employees = Employee.objects.all()
    total_tasks = tasks.count()
    total_employees = employees.count()

    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status='pending').count()
    rejected_tasks = tasks.filter(status='rejected').count()

    total_registered_employees = customers.count()
    context = {'tasks':tasks, 'total_employees': total_employees, "rejected_tasks": rejected_tasks,
        "completed_tasks": completed_tasks, "pending_tasks": pending_tasks,
               "total_tasks": total_tasks,  'date': y , 'myFilter':myFilter}
    return render(request, 'accounts/supervisor.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userPage(request):
    c_tasks=request.user.customer.tasks_set.filter(date_created=date.today())

    print(c_tasks)
    total_tasks=c_tasks.count()
    completed_tasks = c_tasks.filter(status='completed').count()
    pending_tasks = c_tasks.filter(status='pending').count()
    rejected_tasks = c_tasks.filter(status='rejected').count()


    context = { "rejected_tasks":rejected_tasks,"c_tasks": c_tasks, 'pending_tasks':pending_tasks,"total_tasks": total_tasks, "completed_tasks":completed_tasks}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userPending(request):
    c_tasks = request.user.customer.tasks_set.all()
    print(c_tasks)
    pending_tasks = c_tasks.filter(status='pending')


    context={"pending_tasks":pending_tasks,"c_tasks": c_tasks}
    return render(request, 'accounts/userpending.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userPayroll(request):
    c_employees = request.user.customer.employee_set.all()

    context={"c_employees":c_employees}
    return render(request, 'accounts/userpay.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userRejected(request):
    c_tasks = request.user.customer.tasks_set.all()
    rejected_tasks = c_tasks.filter(status='rejected')

    context = {"rejected_tasks": rejected_tasks}
    return render(request, 'accounts/userejected.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userCompleted(request):
    c_tasks = request.user.customer.tasks_set.all()
    completed_tasks = c_tasks.filter(status='completed')

    context = {"completed_tasks": completed_tasks}
    return render(request, 'accounts/usercompleted.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully saved')

    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)





@login_required(login_url='login')
def status(request):
    return render(request, 'accounts/status.html')






