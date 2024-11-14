from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LabourViewSet, AttendanceViewSet, SalaryViewSet
from .views import LabourListView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'labours', LabourViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'salaries', SalaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('api/labours/', LabourListView.as_view(), name='labour-list'),
     
]
