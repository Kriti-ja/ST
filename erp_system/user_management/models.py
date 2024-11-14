from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('sales_manager', 'Sales Manager'),
        ('labour', 'Labour'),
        ('hr', 'HR Department'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Unique name to avoid conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Unique name to avoid conflict
        blank=True,
    )



class Labour(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="labour_profile")
    assigned_sales_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'sales_manager'})
    in_time = models.DateTimeField(null=True, blank=True)
    out_time = models.DateTimeField(null=True, blank=True)

class Attendance(models.Model):
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
