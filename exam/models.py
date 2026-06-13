from django.db import models

# Create your models here.

class Question(models.Model):
    que_id = models.IntegerField(primary_key=True)
    sub_name = models.CharField(max_length=250)
    que_name = models.CharField(max_length=250)
    option_1 = models.CharField(max_length=250)
    option_2 = models.CharField(max_length=250)
    option_3 = models.CharField(max_length=250)
    option_4 = models.CharField(max_length=250)
    correct_ans = models.CharField(max_length=250)
    
    class Meta:
        db_table = 'question'
        
class Stud_Info(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.BigIntegerField()
    role = models.CharField(max_length=20, default='student')
    
    class Meta:
        db_table = 'stud_info'
        
class Result(models.Model):
    username = models.ForeignKey(Stud_Info, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    score = models.IntegerField()
    
    class Meta:
        db_table = 'result'