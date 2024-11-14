from rest_framework import viewsets
from .models import User, Labour, Attendance, Salary
from .serializers import UserSerializer, LabourSerializer, AttendanceSerializer, SalarySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LabourViewSet(viewsets.ModelViewSet):
    queryset = Labour.objects.all()
    serializer_class = LabourSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer


class LabourListView(APIView):
    def get(self, request):
        labours = Labour.objects.all()
        serializer = LabourSerializer(labours, many=True)
        return Response(serializer.data)
