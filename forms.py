from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from .widgets import DatePickerInput
from django import forms
from datetime import date

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude=['user']



class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username','email','password1','password2']

class EmployeeForm(ModelForm):

    class Meta:
        model= Employee
        fields= '__all__'
        exclude=['employee_id']




        widgets={
        'date_of_birth' : DatePickerInput(attrs={'type':'date', 'max':date(2000,1,1)}),
         'joining_date': DatePickerInput(attrs={'type':'date', 'min':date.today()}),
        'termination_date': DatePickerInput(attrs={'type':'date', 'min':date.today()})
        }


class TaskForm(ModelForm):
    class Meta:
        model= Tasks
        fields= '__all__'

class AssetForm(ModelForm):
    class Meta:
        model= Assets
        fields= '__all__'



class LeaveForm(ModelForm):
    start_date = forms.DateField(label='Release year', required=False, widget=forms.DateInput(attrs={'type':'date', 'min':date.today()}))
    end_date = forms.DateField(label='Release year', required=False, widget=forms.DateInput(attrs={'type':'date', 'min':date.today() + timedelta(days=1), 'max':date.today() + timedelta(days=29)}))

    class Meta:
        model = Leave
        fields='__all__'


class ModulesForm(ModelForm):
    class Meta:
        model= Modules
        fields='__all__'


class HealthForm(ModelForm):
    class Meta:
        model=Healthinfo
        fields='__all__'

class WorkapprovalForm(ModelForm):
    class Meta:
        model=work_approval_request
        fields='__all__'
        exclude=['customer']