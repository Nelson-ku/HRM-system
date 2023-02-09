from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Create your models here.

class Customer(models.Model):
     user = models.OneToOneField(User, null=True,blank =True,on_delete=models.CASCADE)
     name = models.CharField(max_length=200,null=True)
     phone = models.CharField(max_length=200,null=True)
     email = models.CharField(max_length=200,null=True)
     profile_pic = models.ImageField( default="/images/",null=True,blank=True)
     date_created=models.DateTimeField(auto_now_add=True,null=True)

     def __str__(self):
          return self.name



class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
         return self.name


class Employee(models.Model):
      ACADEMIC=(
        ('undergraduate','undergraduate'),
        ('Diploma', 'Diploma'),
        ('masters', 'masters')
    )
      GENDER=(
            ('male','male'),
            ('female','female'),
            )


      DEPARTMENT=(
            ('IT','IT'),
            ('PRODUCTION','PRODUCTION'),
            ('SALES', 'SALES'),
            ('INVENTORY', 'INVENTORY'),
            )
      MARITAL= (
          ('SINGLE', 'SINGLE'),
          ('MARRIED', 'MARRIED'),
      )
      customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
      first_name=models.CharField(max_length=20,null=True,validators=[RegexValidator(r'^([a-zA-Z])([a-zA-Z]+)$')],error_messages ={ "validators":"enter a valid name with letters"} )
      middle_name=models.CharField(max_length=20,null=True,validators=[RegexValidator(r'^([a-zA-Z])([a-zA-Z]+)$')])
      last_name = models.CharField(max_length=20, null=True,validators=[RegexValidator(r'^([a-zA-Z])([a-zA-Z]+)$')])
      home_address = models.CharField(max_length=10, null=True,validators=[RegexValidator(r'^([a-zA-Z])([a-zA-Z]+)$')] )
      marital_status = models.CharField(max_length=200, null=True ,choices= MARITAL)
      next_of_kin= models.CharField(max_length=10, null=True,validators=[RegexValidator(r'^([a-zA-Z])([a-zA-Z]+)$')])
      gender=models.CharField(max_length=200, null=True, choices=GENDER)
      academic_level=models.CharField(max_length=200,null=True,choices=ACADEMIC)

      email = models.EmailField(max_length=30, null=True, unique=True)
      contact = models.CharField(max_length=10, null=True, )
      department= models.CharField(max_length=200, null=True, choices=DEPARTMENT)
      citizenship = models.CharField(max_length=200, null=True,validators=[RegexValidator(r'^([a-zA-Z])([a-zA-Z]+)$')])
      joining_date=models.DateField(blank=True, null=True)
      termination_date=models.DateField(blank=True,null=True)
      salary=models.IntegerField(null=True)
      NHIF= models.IntegerField(null=True)
      NSSF = models.IntegerField(null=True)
      date_of_birth=models.DateField(null=True, blank=True)
      upload=models.FileField(null=True,blank=True)
      upload1 = models.FileField(null=True,blank=True)
      upload_pic = models.ImageField(default="post-4.png", null=True, blank=True)



      def __str__(self):
         return self.first_name



class Assets(models.Model):
    Condition = (
        ('good', 'good'),
        ('new ', 'new'),
        ('used', 'used'),

    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    asset_allocated = models.CharField(max_length=200, null=True)
    asset_id = models.CharField(max_length=10, null=True ,unique=True,error_messages ={ "unique":"The asset  you entered is already assigned" })
    date_assigned=models.DateField(auto_now_add=True,null=True)
    condition=models.CharField(max_length=100, null=True, choices=Condition)

class Leave(models.Model):

       LEAVE_TYPE = (
        ('sick Leave ', 'Sick Leave'),
        ('casual leave ', 'Casual Leave'),
        ('Emergency Leave' , 'Emergency Leave'),
        ('Study Leave', 'Study Leave'),
    )
       customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
       start_date =models.DateField(verbose_name= _ ('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
       end_date = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
       reason=models.TextField(max_length=200, null=True, choices=LEAVE_TYPE)









class Modules(models.Model):
    company_upload_file=models.FileField(upload_to='', null=True,blank=True)
    company_file = models.FileField(upload_to='')
    company_policy_file = models.FileField(upload_to='')





class Tasks(models.Model):
    STATUS=(
        ('pending','pending'),
        ('completed', 'completed'),
        ('rejected','rejected')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    weekly_task=models.CharField(null=True, max_length=200)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.weekly_task


class work_approval_request(models.Model):
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    task_id=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=100,null=True)


class Healthinfo(models.Model):
    employee=models.ForeignKey(Employee, null=True,on_delete=models.SET_NULL)
    health_file= models.FileField(null=True, blank=True)







