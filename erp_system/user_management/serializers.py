from rest_framework import serializers
from .models import User, Labour, Attendance, Salary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']

class LabourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labour
        fields = ['id','user', 'assigned_sales_manager', 'in_time', 'out_time']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['labour', 'date', 'status']

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['user', 'amount', 'date']
