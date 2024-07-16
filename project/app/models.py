from django.db import models

# Create your models here.
class Student (models.Model):
 stu_name = models.CharField(max_length=50)
 stu_email = models.EmailField()
 stu_contact = models.IntegerField()
 stu_city = models.TextField(max_length=50)

 def  __str__(self):
  return self.stu_name+' '+self.stu_email
 
 class Meta:
  db_table = 'Student'
  #manage = True
  #varbose_name = 'Student'
  verbose_name_plural = 'Student'
  ordering = ['stu_name']


 
 

