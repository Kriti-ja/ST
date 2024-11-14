from django.contrib import admin
from .models import User, Labour, Attendance, Salary

admin.site.register(User)
admin.site.register(Labour)
admin.site.register(Attendance)
admin.site.register(Salary)
