from django.contrib import admin
from .models import Question, Stud_Info, Result

# Register your models here.
admin.site.register(Question)
admin.site.register(Stud_Info)
admin.site.register(Result)