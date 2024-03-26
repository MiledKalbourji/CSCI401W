from django.shortcuts import render
from rest_framework import viewsets

from .models import Attendance
from .serializers import AttendanceSerializer

# Create your views here.
# views.py


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
